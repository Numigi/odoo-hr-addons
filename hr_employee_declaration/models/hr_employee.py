# © 2018 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta
from itertools import chain
from odoo import api, fields, models, _
from odoo.addons.queue_job.job import job
from odoo.exceptions import ValidationError
from odoo.tools import pycompat


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    declaration_ids = fields.One2many(
        'survey.user_input', string='Declarations',
        compute='_compute_declaration_ids')

    declaration_count = fields.Integer(compute='_compute_declaration_count')

    declaration_survey_id = fields.Many2one(
        'survey.survey', 'Declaration Survey', ondelete='restrict')
    declaration_recipient_id = fields.Many2one(
        'hr.employee', 'Declaration Recipient', ondelete='restrict')
    declaration_mail_template_id = fields.Many2one(
        'mail.template', 'Declaration Email Template', ondelete='restrict')

    periodic_declaration = fields.Boolean()
    declaration_next_date = fields.Date('Next Declaration Date')
    declaration_periodicity = fields.Selection([
        ('month', 'Month'),
        ('year', 'Year'),
    ])

    def _compute_declaration_ids(self):
        for employee in self:
            employee.declaration_ids = self.env['survey.user_input'].search([
                '|',
                ('declaration_employee_id', '=', employee.id),
                '&',
                ('declaration_employee_id', '=', False),
                ('partner_id.user_ids.employee_ids', '=', employee.id),
            ])

    def _compute_declaration_count(self):
        for employee in self:
            employee.declaration_count = len(employee.declaration_ids)

    @api.multi
    def send_due_declaration_surveys_by_email(self):
        """Send every due employee declarations by email."""
        today = fields.Date.to_string(datetime.now())

        active_jobs = self.env['queue.job'].search([
            ('model_name', '=', 'hr.employee'),
            ('method_name', '=', 'send_declaration_survey_by_email'),
            ('state', '!=', 'done'),
        ])
        employee_ids_with_active_jobs = list(chain(*active_jobs.mapped('record_ids')))

        employees_with_declarations_to_send = self.search([
            ('declaration_next_date', '<=', today),
            ('id', 'not in', employee_ids_with_active_jobs),
        ])

        for employee in employees_with_declarations_to_send:
            employee.with_delay().send_declaration_survey_by_email()

    @job
    def send_declaration_survey_by_email(self):
        """Send the declaration by email to a single employee.

        This method reproduces the behavior found in the module survey at
        survey/wizard/survey_email_compose_message.py

        When sending the email, the body is parsed, and the string __URL__ is
        replaced with the url and token of the survey form.
        """
        template = self._get_declaration_mail_template()
        user_input = self._generate_declaration_survey_user_input()

        body = template.generate_email(user_input.id, ['body_html'])['body_html']
        body_with_token = self._add_token_to_declaration_body(body, user_input)

        template.send_mail(
            user_input.id, force_send=True, raise_exception=True,
            email_values={
                'body': body_with_token,
                'body_html': body_with_token,
                'partner_ids': [(4, user_input.partner_id.id)],
            })

        if self.periodic_declaration:
            self._compute_declaration_next_date()

    def _add_token_to_declaration_body(self, body, user_input):
        url_with_token = '{}/{}'.format(user_input.survey_id.public_url, user_input.token)

        if '__URL__' not in body:
            raise ValidationError(_(
                'Could not send the email for the employee declaration of {employee}. '
                'The body of the email template does not contain __URL__.'
            ).format(employee=self.display_name))

        return body.replace('__URL__', url_with_token)

    def _generate_declaration_survey_user_input(self):
        token = pycompat.text_type(uuid.uuid4())
        recipient = self._get_declaration_recipient()
        survey = self._get_declaration_survey()
        user_input = self.env['survey.user_input'].create({
            'survey_id': survey.id,
            'date_create': fields.Datetime.now(),
            'type': 'link',
            'state': 'new',
            'token': token,
            'partner_id': recipient.id,
            'email': recipient.email,
            'declaration_employee_id': self.id,
        })
        return user_input

    def _get_declaration_recipient(self):
        """Get the partner who should fill the employee's declaration.

        :rtype: res.partner singleton
        """
        recipient_employee = self.declaration_recipient_id or self

        if not recipient_employee.user_id:
            raise ValidationError(_(
                'The employee declaration could not be sent to {recipient} '
                'because this person is not linked to a user.'
            ).format(recipient=recipient_employee.display_name))

        return recipient_employee.user_id.partner_id

    def _get_declaration_survey(self):
        """Get the survey to use for the employee declaration.

        :rtype: survey.survey singleton
        """
        if not self.declaration_survey_id:
            raise ValidationError(_(
                'The employee declaration could not be sent to {employee} '
                'because the employee has no declaration survey set.'
            ).format(employee=self.display_name))

        return self.declaration_survey_id

    def _get_declaration_mail_template(self):
        """Get the mail template to use for the employee declaration.

        :rtype: mail.template singleton
        """
        if not self.declaration_mail_template_id:
            raise ValidationError(_(
                'The employee declaration could not be sent to {employee} '
                'because the employee has no mail template defined for this.'
            ).format(employee=self.display_name))

        recipient = self._get_declaration_recipient()
        return self.declaration_mail_template_id.with_context(lang=recipient.lang)

    def _get_declaration_email_context(self):
        """Get the context used for rendering the declaration email template."""
        return {
            'employee': self,
            'recipient': self._get_declaration_recipient(),
        }

    def _compute_declaration_next_date(self):
        previous_date = fields.Date.from_string(self.declaration_next_date)
        delta = (
            relativedelta(months=1) if self.declaration_periodicity == 'month'
            else relativedelta(years=1)
        )
        self.declaration_next_date = previous_date + delta

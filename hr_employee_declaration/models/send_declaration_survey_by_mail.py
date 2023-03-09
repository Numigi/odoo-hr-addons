# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import uuid

import werkzeug
from odoo import fields, models, _
from odoo.exceptions import ValidationError


class HrEmployeeWithSendDeclarations(models.Model):
    _inherit = 'hr.employee'

    declaration_survey_id = fields.Many2one(
        'survey.survey', 'Declaration Survey', ondelete='restrict')
    declaration_recipient_id = fields.Many2one(
        'hr.employee', 'Declaration Recipient', ondelete='restrict')
    declaration_mail_template_id = fields.Many2one(
        'mail.template', 'Declaration Email Template', ondelete='restrict')

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

    def _add_token_to_declaration_body(self, body, user_input):
        url_with_token = '%s?%s' % (user_input.survey_id.get_start_url(), werkzeug.urls.url_encode(
            {'answer_token': user_input and user_input.access_token or None}))

        if '__URL__' not in body:
            raise ValidationError(_(
                'Could not send the email for the employee declaration of {employee}. '
                'The body of the email template does not contain __URL__.'
            ).format(employee=self.display_name))

        return body.replace('__URL__', url_with_token)

    def _generate_declaration_survey_user_input(self):
        token = str(uuid.uuid4())
        recipient = self._get_declaration_recipient()
        survey = self._get_declaration_survey()
        user_input = self.env['survey.user_input'].create({
            'survey_id': survey.id,
            'state': 'new',
            'access_token': token,
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

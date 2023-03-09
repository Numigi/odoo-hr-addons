# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from datetime import datetime
from dateutil.relativedelta import relativedelta
from itertools import chain
from odoo import fields, models


class HrEmployeeWithDeclarationEmailCron(models.Model):
    """Add a cron to automatically send the employee declarations."""

    _inherit = 'hr.employee'

    periodic_declaration = fields.Boolean()
    declaration_next_date = fields.Date('Next Declaration Date')
    declaration_periodicity = fields.Selection([
        ('month', 'Month'),
        ('year', 'Year'),
    ])

    def send_due_declaration_surveys_by_email(self):
        """Send every due employee declarations by email."""
        today = fields.Date.to_string(datetime.now())

        active_jobs = self.env['queue.job'].search([
            ('model_name', '=', 'hr.employee'),
            ('method_name', '=', 'send_declaration_survey_by_email'),
            ('state', '!=', 'done'),
        ])
        employee_ids_with_active_jobs = list(chain(
            *active_jobs.mapped('record_ids')))

        employees_with_declarations_to_send = self.search([
            ('declaration_next_date', '<=', today),
            ('id', 'not in', employee_ids_with_active_jobs),
        ])

        for employee in employees_with_declarations_to_send:
            employee.with_delay().send_declaration_survey_by_email()

    def send_declaration_survey_by_email(self):
        """Send the employee declaration by email."""
        super().send_declaration_survey_by_email()
        if self.periodic_declaration:
            self._compute_declaration_next_date()

    def _compute_declaration_next_date(self):
        previous_date = fields.Date.from_string(self.declaration_next_date)
        delta = (
            relativedelta(months=1) if self.declaration_periodicity == 'month'
            else relativedelta(years=1)
        )
        self.declaration_next_date = previous_date + delta

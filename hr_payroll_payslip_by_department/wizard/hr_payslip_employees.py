# Copyright 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrPayslipEmployees(models.TransientModel):
    _inherit = "hr.payslip.employees"

    @api.model
    def _get_default_employees(self):
        department_ids = self.env.context.get("department_ids")
        # Get the list part of the tuple containing the ids of department
        department_ids = department_ids[0][2]
        return (
            self.env["hr.employee"]
            .search([("department_id", "in", department_ids)])
            .ids
        )

    employee_ids = fields.Many2many(
        default=lambda self: self._get_default_employees(),
    )

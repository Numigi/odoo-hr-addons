# © 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HrPayslipEmployees(models.TransientModel):
    _inherit = "hr.payslip.employees"

    employee_ids = fields.Many2many(
        "hr.employee",
        "hr_employee_group_rel",
        "payslip_id",
        "employee_id",
        "Employees",
        default=lambda self: self.get_default_employees(),
    )

    @api.model
    def get_default_employees(self):
        departments = self.env.context.get("department_ids", [(6, 0, [])])

        department_ids = departments[0][2]
        return (
            self.env["hr.employee"]
            .search([("department_id", "in", department_ids)])
            .ids
        )

# Copyright 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    department_ids = fields.Many2many("hr.department", string="Departments")

    @api.multi
    def get_payslip_employees_wizard(self):
        """
        Inherit this method from the OCA Module hr_payroll to add the
        employees of the selected departments to the default value of the
        employee_ids field in the wizard.
        """
        res = super(HrPayslipRun, self).get_payslip_employees_wizard()

        if self.department_ids:
            employee_ids = self.env["hr.employee"].browse(
                res["context"]["default_employee_ids"][0][2]
            )
            if employee_ids:
                employee_filtered_ids = employee_ids.filtered(
                    lambda e: e.department_id in self.department_ids
                ).ids
                res["context"]["default_employee_ids"] = [(6, 0, employee_filtered_ids)]

        return res

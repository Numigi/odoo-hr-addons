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

        res = super().get_payslip_employees_wizard()
        company = self.company_id
        domain = [('company_id', '=', company.id)]
        if self.department_ids:
            domain.append(('department_id', 'in', self.department_ids.ids))
        employee_ids = self.env['hr.employee'].search(domain)
        emp_ids = []
        for emp in employee_ids:
            if (emp.contract_id.schedule_pay == self.schedule_pay
                    and emp.contract_id.state == 'open') :
                emp_ids.append(emp.id)
        res["context"]["default_employee_ids"] = [(6, 0, emp_ids)]
        return res

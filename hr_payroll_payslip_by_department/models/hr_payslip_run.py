# Copyright 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrPayslipRun(models.Model):
    _inherit = 'hr.payslip.run'

    department_ids = fields.Many2many('hr.department', string='Departments')

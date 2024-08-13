# © 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api

class HrPayslipRun(models.Model):
    _inherit = 'hr.payslip.run'

    department_ids = fields.Many2many('hr.department', string='Departments')
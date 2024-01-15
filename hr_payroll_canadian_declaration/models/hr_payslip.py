# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class HrPayslipLine(models.Model):

    _inherit = 'hr.payslip.line'

    t4_box = fields.Text(related='salary_rule_id.t4_box', index=True, store=True, string="T4 Box")
    r1_box = fields.Text(related='salary_rule_id.r1_box', index=True, store=True, string="R1 Box")

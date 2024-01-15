# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models,fields


class HrPayslipLine(models.Model):

    _inherit = 'hr.salary.rule'

    t4_box = fields.Text("T4 Box")
    r1_box = fields.Text("R1 Box")

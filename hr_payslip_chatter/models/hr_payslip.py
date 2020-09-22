# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class Payslip(models.Model):
    _inherit = ['hr.payslip', 'mail.activity.mixin', 'mail.thread']
    _name = 'hr.payslip'

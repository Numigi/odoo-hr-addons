# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ContractWithWageType(models.Model):

    _inherit = 'hr.contract'

    wage_type = fields.Selection([
        ('hour', 'Hour'),
        ('month', 'Month'),
        ('year', 'Year'),
    ])

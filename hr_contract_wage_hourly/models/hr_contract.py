# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Contract(models.Model):

    _inherit = 'hr.contract'

    hourly_wage = fields.Monetary(digits=(16, 2), track_visibility="onchange")

# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class EventType(models.Model):

    _name = "hr.event.type"
    _description = "HR Event Type"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)

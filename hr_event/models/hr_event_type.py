# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class EventType(models.Model):

    _name = "hr.event.type"
    _description = "Event Type"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)

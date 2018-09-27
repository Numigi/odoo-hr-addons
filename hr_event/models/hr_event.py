# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Event(models.Model):

    _name = "hr.event"
    _description = "HR Event"
    _rec_name = "description"

    employee_id = fields.Many2one(
        "hr.employee", "Employee", required=True, ondelete="restrict", index=True)
    date = fields.Datetime(required=True, index=True, default=fields.Datetime.now)
    type_id = fields.Many2one(
        "hr.event.type", "Type", required=True, ondelete="restrict", index=True)
    description = fields.Char(required=True)
    notes = fields.Text()

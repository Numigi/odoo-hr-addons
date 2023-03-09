# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrAttendanceChatter(models.Model):
    _name = "hr.attendance"
    _inherit = ['hr.attendance', 'mail.thread']

    employee_id = fields.Many2one(track_visibility='always')
    check_in = fields.Datetime(track_visibility='onchange')
    check_out = fields.Datetime(track_visibility='onchange')
    working_space_id = fields.Many2one(track_visibility='always')

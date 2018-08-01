# -*- coding: utf-8 -*-
# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HRWorkingSpace(models.Model):
    """ Add working spaces to attendance"""
    _inherit = "hr.attendance"

    working_space_id = fields.Many2one('hr.working.space', string='Working Space', require=True)


class HREmployeeWorkingSpace(models.Model):
    """ Add the management of the working space at the attendance."""
    _inherit = 'hr.employee'

    @api.multi
    def attendance_manual_working_space(self, next_action, working_space_id=None, entered_pin=None):
        res = self.attendance_manual(next_action, entered_pin=entered_pin)
        if working_space_id:
            attendance = self.env['hr.attendance'].search([('id', '=', res['action']['attendance']['id'])], limit=1)
            attendance.working_space_id = working_space_id
        return res

# -*- coding: utf-8 -*-
# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HRWorkingSpace(models.Model):
    _inherit = "hr.attendance"

    niko_id = fields.Many2one(
        'hr.niko.niko',
        string='Niko-niko mood'
    )


class HREmployeeWorkingSpace(models.Model):
    _inherit = 'hr.employee'

    @api.multi
    def attendance_manual_niko_niko(self, next_action, niko_id=None, entered_pin=None):
        res = self.attendance_manual(
            next_action,
            entered_pin=entered_pin
        )
        if niko_id:
            attendance = self.env['hr.attendance'].search(
                [('id', '=', res['action']['attendance']['id'])], limit=1
            )
            attendance.niko_id = niko_id
        return res

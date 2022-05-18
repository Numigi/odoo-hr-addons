# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api


class ResourceNiko(models.Model):
    _inherit = "hr.employee"

    niko_time = fields.Boolean(
        string="Niko attendance time", compute="get_niko_time", store=True
    )

    @api.multi
    def attendance_manual_mood_id(self, next_action, mood_id=None, entered_pin=None):
        res = self.attendance_manual(next_action, entered_pin=entered_pin)
        if mood_id:
            attendance = self.env["hr.attendance"].search(
                [("id", "=", res["action"]["attendance"]["id"])], limit=1
            )
            attendance.niko_id = mood_id
        return res

    @api.depends("resource_calendar_id.ask_niko")
    def get_niko_time(self):
        for employee in self:
            calendar_id = employee.resource_calendar_id
            if calendar_id.ask_niko:
                employee.niko_time = False
                date = datetime.now()
                hour_s = date.hour * 3600
                minut_s = date.minute * 60
                total_second = hour_s + minut_s + date.second
                flt_time = round(total_second / 3600, 2)
                employee.niko_time = (
                    True
                    if flt_time >= calendar_id.begin_time
                    and flt_time <= calendar_id.end_time
                    else False
                )

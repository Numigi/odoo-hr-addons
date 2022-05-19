# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api


class ResourceNiko(models.Model):
    _inherit = "hr.employee"

    @api.multi
    def attendance_manual_mood_id(self, next_action, mood_id=None, entered_pin=None):
        res = self.attendance_manual(next_action, entered_pin=entered_pin)
        if mood_id:
            attendance = self.env["hr.attendance"].search(
                [("id", "=", res["action"]["attendance"]["id"])], limit=1
            )
            attendance.niko_id = mood_id
        return res

    @api.multi
    def get_niko_time(self, user_id):
        datas = []
        res = {}
        employee = self.search([("user_id", "=", user_id)], limit=1)
        calendar_id = employee.resource_calendar_id
        if calendar_id.ask_niko:
            date = datetime.now()
            hour_s = date.hour * 3600
            minut_s = date.minute * 60
            total_second = hour_s + minut_s + date.second
            flt_time = round(total_second / 3600, 2)
            res["nikotime"] = (
                True
                if flt_time >= calendar_id.begin_time
                and flt_time <= calendar_id.end_time
                else False
            )
            res["moods"] = self.env["hr.niko"].search_read(
                [], fields=["name", "icon"], order="sequence"
            )
        datas.append(res)
        return datas

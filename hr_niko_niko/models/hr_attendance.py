# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HRNikoNiko(models.Model):
    """Add Niko to attendance"""

    _inherit = "hr.attendance"

    niko_niko_id = fields.Many2one("hr.niko.niko", string="Mood", require=True)


class HREmployeeNikoNiko(models.Model):
    """Add the management of Niko at the attendance."""

    _inherit = "hr.employee"

    niko_niko = fields.Boolean(
        string="Request the Niko Niko",
        related="resource_calendar_id.niko_niko",
        store=True,
        readonly=True,
    )
    niko_from = fields.Float(
        string="From",
        related="resource_calendar_id.niko_from",
        store=True,
        readonly=True,
    )
    niko_to = fields.Float(
        string="To",
        related="resource_calendar_id.niko_to",
        store=True,
        readonly=True,
    )

    @api.multi
    def attendance_manual_niko(self, next_action, niko_niko_id=None, entered_pin=None):
        res = self.attendance_manual(next_action, entered_pin=entered_pin)
        if niko_niko_id:
            attendance = self.env["hr.attendance"].search(
                [("id", "=", res["action"]["attendance"]["id"])], limit=1
            )
            attendance.niko_niko_id = niko_niko_id
        return res


class ResourceCalendar(models.Model):
    _inherit = "resource.calendar"

    niko_niko = fields.Boolean(string="Request the Niko Niko")
    niko_from = fields.Float(string="From")
    niko_to = fields.Float(string="To")

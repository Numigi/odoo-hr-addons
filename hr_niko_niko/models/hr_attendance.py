# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    niko_id = fields.Many2one(
        "hr.niko",
        string="Mood",
    )

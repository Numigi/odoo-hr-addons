# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ResourceNiko(models.Model):
    _inherit = "resource.calendar"

    ask_niko = fields.Boolean(string="Ask for the Niko-niko")
    begin_time = fields.Float(string="From")
    end_time = fields.Float(string="To")

    @api.constrains("begin_time", "end_time")
    def _check_time_niko(self):
        for s in self:
            if s.begin_time > s.end_time:
                raise ValidationError(_("Please Check your interval time."))

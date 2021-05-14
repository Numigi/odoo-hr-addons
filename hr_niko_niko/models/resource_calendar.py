# -*- coding: utf-8 -*-
# © 2021 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResourceCalendar(models.Model):
    _inherit = "resource.calendar"

    start_time = fields.Float(
        string='From'
    )
    end_time = fields.Float(
        string='To'
    )

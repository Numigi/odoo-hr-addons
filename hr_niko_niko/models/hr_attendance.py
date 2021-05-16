# -*- coding: utf-8 -*-
# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HRWorkingSpace(models.Model):
    _inherit = "hr.attendance"

    niko_id = fields.Many2one(
        'hr.niko.niko',
        string='Niko-niko mood',
        ondelete='restrict'
    )


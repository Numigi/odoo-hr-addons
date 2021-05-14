# -*- coding: utf-8 -*-
# © 2021 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrNikoNiko(models.Model):
    _name = "hr.niko.niko"
    _description = "HR niko niko"
    _order = "sequence"

    active = fields.Boolean(
        string='Active',
        default=True
    )
    name = fields.Char(
        string='Name',
        required=True,
        translate=True
    )
    sequence = fields.Integer(
        string='Sequence',
        required=True,
        default=10
    )
    icon = fields.Char(
        string='Icon'
    )

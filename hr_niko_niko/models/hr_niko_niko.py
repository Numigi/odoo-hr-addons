# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrNiko(models.Model):
    _name = "hr.niko"
    _description = "HR Mood Niko"

    name = fields.Char("Name")
    icon = fields.Char(
        "Icon",
        help="Font Awesome code of the icon that will represent the Mood Niko. See https://fontawesome.com/icons?d=gallery.",
    )
    active = fields.Boolean(string="Active", default=True)
    sequence = fields.Integer(string="sequence")

    _sql_constraints = [
        (
            "sequence",
            "unique (sequence)",
            "The Sequence must be unique, this one is already assigned to another record.",
        )
    ]

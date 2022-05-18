# -*- coding: utf-8 -*-

from odoo import fields, models


class HRAttendanceWithNikoNiko(models.Model):
    """Basic definition of Niko Niko"""

    _name = "hr.niko.niko"
    _description = "HR Niko Niko"
    _order = 'sequence'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    icon = fields.Char(
        "Icon",
        help="Font Awesome code of the icon that will represent the working space. See https://fontawesome.com/icons?d=gallery.",
    )
    sequence = fields.Integer(string="Sequence", default=10)

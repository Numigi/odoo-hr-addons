# -*- coding: utf-8 -*-
# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HRAttendanceWithWorkingSpace(models.Model):
    """ Basic definition of a workspace"""
    _name = "hr.working.space"
    _description = "HR Working Space"

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    icon = fields.Char(
        "Icon",
        help="Font Awesome code of the icon that will represent the working space. "
        "See https://fontawesome.com/icons?d=gallery."
    )

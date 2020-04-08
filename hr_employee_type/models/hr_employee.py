# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields, api


class HrEmployeeType(models.Model):
    _inherit = "hr.employee"
    ttype = fields.Selection(
        [("internal", "Internal"), ("external", "External")],
        "Type",
        default="internal",
    )

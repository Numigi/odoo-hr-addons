# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class HrEmployeeType(models.Model):
    _inherit = "hr.employee"
    ttype = fields.Selection(
        [("internal", "Internal"), ("external", "External")],
        "Type",
        default=lambda record: record._context.get("search_default_ttype", "internal")
    )

# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class HrEmployeeType(models.Model):
    _inherit = "hr.employee"
    ttype = fields.Selection(
        [("internal", "Internal"), ("external", "External")],
        "Type",
        default="internal",
        groups="hr.group_hr_user",
    )

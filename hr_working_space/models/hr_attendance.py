# Copyright 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HRWorkingSpace(models.Model):
    """Add working spaces to attendance"""

    _inherit = "hr.attendance"

    working_space_id = fields.Many2one(
        "hr.working.space", string="Working Space", required=True
    )

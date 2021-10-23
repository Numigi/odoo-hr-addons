# © 2021 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class Contract(models.Model):

    _inherit = "hr.contract"

    equivalent_wage = fields.Float(compute="_compute_equivalent_wage")
    equivalent_wage_type = fields.Selection(
        [
            ("hour", "Hour"),
            ("year", "Year"),
        ],
        compute="_compute_equivalent_wage",
    )

    @api.depends("resource_calendar_id", "wage", "wage_type")
    def _compute_equivalent_wage(self):
        for contract in self:
            contract.equivalent_wage_type = contract._get_equivalent_wage_type()
            contract.equivalent_wage = contract._get_equivalent_wage()

    def _get_equivalent_wage_type(self):
        return "year" if self.wage_type == "hour" else "hour"

    def _get_equivalent_wage(self):
        if self.wage_type == "hour":
            return self.wage * self._get_hours_per_week() * 52

        elif self.wage_type == "year":
            return self.wage / (self._get_hours_per_week() * 52)

    def _get_hours_per_week(self):
        return self.resource_calendar_id.hours_per_week or 0

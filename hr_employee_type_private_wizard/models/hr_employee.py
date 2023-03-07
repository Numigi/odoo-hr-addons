# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models, _
from odoo.exceptions import AccessError


class Employee(models.Model):

    _inherit = "hr.employee"

    @api.model
    def create(self, vals):
        employee = super().create(vals)
        employee.sudo()._propagate_employee_type_to_home_address()
        return employee

    def write(self, vals):
        super().write(vals)

        if "ttype" in vals:

            self._check_user_can_change_employee_type()

            for employee in self:
                employee.sudo()._propagate_employee_type_to_home_address()

        return True

    def _propagate_employee_type_to_home_address(self):
        home_address = self.address_home_id
        if home_address and self.ttype != home_address.employee_type:
            home_address.employee_type = self.ttype

    def _check_user_can_change_employee_type(self):
        if not self.env.user.has_private_data_access():
            raise AccessError(_(
                "You are not allowed to change the type of an employee."
            ))

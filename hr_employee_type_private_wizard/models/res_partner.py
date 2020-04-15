# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, _
from odoo.exceptions import AccessError
from odoo.osv.expression import OR


class Partner(models.Model):

    _inherit = 'res.partner'

    employee_type = fields.Selection(
        [
            ("internal", "Internal"),
            ("external", "External"),
        ]
    )

    def get_private_address_access_domain(self):
        domain = super().get_private_address_access_domain()

        if self.env.user.has_internal_employee_access():
            domain = OR((domain, [("employee_type", "=", "internal")]))

        if self.env.user.has_external_employee_access():
            domain = OR((domain, [("employee_type", "=", "external")]))

        return domain

    def check_private_address_access(self):
        if self._is_internal_employee_address():
            return self._check_internal_employee_private_address_access()

        elif self._is_external_employee_address():
            return self._check_external_employee_private_address_access()

        else:
            return super().check_private_address_access()

    def _is_internal_employee_address(self):
        return self.type == "private" and self.employee_type == "internal"

    def _is_external_employee_address(self):
        return self.type == "private" and self.employee_type == "external"

    def _check_internal_employee_private_address_access(self):
        if not self.env.user.has_internal_employee_access():
            raise AccessError(
                _(
                    "You are not allowed to access this partner "
                    "because it is the home address of an internal employee."
                )
            )

    def _check_external_employee_private_address_access(self):
        if not self.env.user.has_external_employee_access():
            raise AccessError(
                _(
                    "You are not allowed to access this partner "
                    "because it is the home address of an external employee."
                )
            )

# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, _
from odoo.exceptions import AccessError


class EmployeePrivateWizard(models.TransientModel):

    _inherit = "hr.employee.private.wizard"

    def check_extended_security_all(self):
        for wizard in self:
            if (
                wizard._is_internal_employee()
                and not self.env.user.has_internal_employee_access()
            ):
                raise AccessError(
                    _(
                        "You are not allowed to access private information of internal employees."
                    )
                )

            if (
                wizard._is_external_employee()
                and not self.env.user.has_external_employee_access()
            ):
                raise AccessError(
                    _(
                        "You are not allowed to access private information of external employees."
                    )
                )

    def _is_internal_employee(self):
        return self._get_employee().ttype == "internal"

    def _is_external_employee(self):
        return self._get_employee().ttype == "external"

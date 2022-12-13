# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class User(models.Model):

    _inherit = 'res.users'

    def has_internal_employee_access(self):
        return self.has_group(
            "hr_employee_type_private_wizard.group_internal"
        )

    def has_external_employee_access(self):
        return self.has_group(
            "hr_employee_type_private_wizard.group_external"
        )

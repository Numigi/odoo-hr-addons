# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class Employee(models.Model):

    _inherit = "hr.employee"

    def action_open_private_data_wizard(self):
        wizard = self.env["hr.employee.private.wizard"].create(
            {"employee_id": self.id,}
        )
        action = wizard.get_formview_action()
        action["target"] = "new"
        return action

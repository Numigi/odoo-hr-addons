# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models, _
from odoo.exceptions import ValidationError


class Contract(models.Model):

    _inherit = 'hr.contract'

    @api.constrains('state', 'active', 'employee_id')
    def _check_single_open_contract_per_employee(self):
        open_contracts = self.filtered(lambda c: c._is_open())

        for contract in open_contracts:
            other_open_contracts = contract.employee_id.contract_ids.filtered(
                lambda c: c._is_open() and c != contract
            )
            if other_open_contracts:
                raise ValidationError(_(
                    'Only one open (running) contract is allowed per employee. '
                ))

    def _is_open(self):
        return self.state == 'open' and self.active

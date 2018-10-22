# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models, _
from odoo.exceptions import ValidationError
from odoo.tools import float_compare


class LeaveRequestWithHalfDayConstraint(models.Model):

    _inherit = 'hr.holidays'

    @api.constrains('number_of_days_temp')
    def _check_number_of_days_is_multiple_of_half_day(self):
        for leave in self:
            if float_compare(leave.number_of_days_temp % 0.5, 0, precision_digits=2):
                raise ValidationError(_(
                    "The number of days of leave requested does not comply "
                    "with the company's leave policy. "
                    "You must express your request in whole days or half days "
                    "(roundings of 0.5)."
                ))

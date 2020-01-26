# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import logging
from odoo import models, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrExpenseSheetConstrain(models.Model):
    _inherit = 'hr.expense.sheet'

    @api.constrains('expense_line_ids')
    def _are_expenses_same_months(self):
        for record in self:
            months = {line.date.month for line in record.expense_line_ids}

            if len(months) > 1:
                raise ValidationError(_(
                    "All expenses must be from the same month."
                    " Please review the list of expenses."
                ))

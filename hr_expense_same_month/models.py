# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import logging
from odoo import models, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrExpenseSheetConstrain(models.Model):
    _inherit = 'hr.expense.sheet'

    @api.model
    def create(self, vals_list):
        if not self._are_expenses_same_months(vals_list):
            self._raise_expenses_error()

        return super().create(vals_list)

    @api.multi
    def write(self, vals):
        if not self._are_expenses_same_months(vals):
            self._raise_expenses_error()

        return super().write(vals)

    def _are_expenses_same_months(self, vals):
        expense_line_field = "expense_line_ids"

        if expense_line_field in vals:
            expenses = []

            for line in vals[expense_line_field]:
                expense_details = line[-1]

                if isinstance(expense_details, list):
                    expenses.extend(expense_details)
                else:
                    expenses.append(expense_details)

            months = self._expense_months(expenses)
            return not len(months) > 1
        return True

    def _expense_months(self, expenses):
        months = set()
        for entry in expenses:

            if isinstance(entry, dict):
                # date is required in hr.expense
                date = entry["date"]
                month = date.split("-")[1]
                months.add(month)

            else:
                expense = self.env["hr.expense"].browse(entry)
                if expense:
                    months.add(expense.date.month)

        return months

    @staticmethod
    def _raise_expenses_error():
        raise ValidationError(_(
            "All expenses must be from the same month. Please review the list of expenses."
        ))

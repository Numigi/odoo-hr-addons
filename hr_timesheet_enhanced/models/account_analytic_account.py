# © 2022 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    def unlink(self):
        context = dict(self.env.context or {})
        self -= self.with_context(active_test=False).filtered(
            lambda account: account.project_ids and "delete_project" in context
        )
        return super(AccountAnalyticAccount, self).unlink()

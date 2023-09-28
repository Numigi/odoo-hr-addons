# © 2023 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class Project(models.Model):
    _inherit = "project.project"

    is_timesheet = fields.Boolean(
        string="Has timesheets",
        compute="_compute_is_timesheet",
        compute_sudo=True,
        store=True,
    )

    @api.depends(
        "tasks",
        "tasks.project_id",
        "tasks.timesheet_ids",
        "tasks.timesheet_ids.project_id",
        "analytic_account_id",
        "analytic_account_id.line_ids",
        "analytic_account_id.line_ids.project_id",
    )
    def _compute_is_timesheet(self):
        for project in self:
            project.is_timesheet = project.with_context(active_test=False).tasks.mapped(
                "timesheet_ids"
            ).filtered(
                lambda timesheet: timesheet.project_id & project
            ) or project.analytic_account_id.line_ids.filtered(
                lambda line: line.project_id & project
            )

    def write(self, vals):
        if "analytic_account_id" in vals:
            self._account_analytic_change()
        res = super(Project, self).write(vals)

        if "active" in vals:
            self._account_analytic_change_active(vals)

        return res

    def _account_analytic_change(self):
        for project in self.filtered(
            lambda project: project.is_timesheet and project.analytic_account_id
        ):
            raise UserError(
                _(
                    """Project %s can't change its analytic account,
                    because it has timesheets associated."""
                    % project.name
                )
            )

    def _account_analytic_change_active(self, vals):
        if vals["active"]:
            self.mapped("analytic_account_id").write({"active": True})

        else:
            self.mapped("analytic_account_id").filtered(
                lambda account: not account.line_ids and not account.project_ids
            ).write({"active": False})

    def unlink(self):
        return super(Project, self.with_context(delete_project=True)).unlink()

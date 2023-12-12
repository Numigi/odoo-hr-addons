# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrPayslipLine(models.Model):
    _inherit = "hr.payslip.line"

    period_id = fields.Many2one(
        "hr.period",
        "Period",
        related="slip_id.hr_period_id",
        store=True,
    )
    start_date = fields.Date(
        "Start Date",
        related="slip_id.date_from",
        store=True,
    )
    end_date = fields.Date(
        "End Date",
        related="slip_id.date_to",
        store=True,
    )
    payslip_state = fields.Selection(
        "Payslip Status",
        related="slip_id.state",
        store=True,
    )
    department_id = fields.Many2one(
        "hr.department",
        "Department",
        related="slip_id.employee_id.department_id",
        store=True,
    )

# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class HrPayslip(models.Model):

    _inherit = 'hr.payslip'

    def compute_sheet(self):
        super(HrPayslip, self).compute_sheet()
        for payslip in self:
            for line in payslip.line_ids:
                if not line.salary_rule_id.t4_box and not line.salary_rule_id.r1_box:
                    continue
                line.t4_box = line.salary_rule_id.t4_box
                line.r1_box = line.salary_rule_id.r1_box


class HrPayslipLine(models.Model):

    _inherit = 'hr.payslip.line'

    t4_box = fields.Text("T4 Box")
    r1_box = fields.Text("R1 Box")

    @api.model
    def compute_canadian_declaration(self, replace_all=False):
        """
        This function compute R1 and T4 box for payslip lines.
        Lines having a R1 and T4 values are not recomputed.
        :return:
        """
        payslip_lines = self.search(['|', ('salary_rule_id.r1_box', '!=', False),
                                     ('salary_rule_id.t4_box', '!=', False)])
        for rec in payslip_lines:
            if replace_all:
                rec.t4_box = rec.salary_rule_id.t4_box
                rec.r1_box = rec.salary_rule_id.r1_box
            else:
                if not rec.t4_box and rec.salary_rule_id.t4_box:
                    rec.t4_box = rec.salary_rule_id.t4_box
                if not rec.r1_box and rec.salary_rule_id.r1_box:
                    rec.r1_box = rec.salary_rule_id.r1_box
        return True







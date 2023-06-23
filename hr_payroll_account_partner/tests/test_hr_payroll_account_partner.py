# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from .common import PayrollPreparationToPayslipCase


class TestPayslip(PayrollPreparationToPayslipCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.payslip = cls.env["hr.payslip"].create(
            {
                "employee_id": cls.employee.id,
                "company_id": cls.company.id,
                "contract_id": cls.contract.id,
                "struct_id": cls.structure.id,
                "date_from": cls.date_start,
                "date_to": cls.date_end,
                "credit_note": True,
                "journal_id": cls.journal.id,
            }
        )
        cls.rule = cls.env.ref("hr_payroll.hr_rule_basic")
        cls.rule.write(
            {
                "amount_select": "code",
                "amount_python_compute": "result = entries.AAA",
            }
        )
        cls.structure.rule_ids[0].write({
            'account_debit': cls.account_debit.id,
        })
        cls.structure.rule_ids[1].write({
            'account_credit': cls.account_credit.id,
        })

    def test_00_move_lines_partner_application(self):
        """Check the correct conditioning on the application of the partner
         in the lines of accounting entries from the payslip lines"""
        self.payslip.compute_sheet()
        self.payslip.action_payslip_done()
        move_lines_partner = \
            self.payslip.move_id.line_ids.mapped('partner_id')
        assert len(move_lines_partner) == 1 and \
               self.employee_address in move_lines_partner

    def test_11_move_lines_partner_application(self):
        """Check the correct conditioning on the application of the partner
         in the lines of accounting entries from the payslip lines"""
        self.rule.write(
            {
                "amount_select": "code",
                "amount_python_compute": "result = entries.AAA",
            }
        )
        self.payslip.compute_sheet()
        self.payslip.line_ids.mapped('salary_rule_id').write({
            'register_id': self.register.id,
        })
        self.payslip.action_payslip_done()
        move_lines_partner = \
            self.payslip.move_id.line_ids.mapped('partner_id')
        assert len(move_lines_partner) == 1 and \
               self.register_address in move_lines_partner

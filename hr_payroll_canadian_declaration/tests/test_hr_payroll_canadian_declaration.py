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
                "contract_id": cls.contract.id,
                "struct_id": cls.structure.id,
                "date_from": cls.date_start,
                "date_to": cls.date_end,

            }
        )
        cls.rule_a = cls.env.ref('hr_payroll.hr_salary_rule_houserentallowance1')

    def test_00_compute_new_canadian_declaration_box(self):
        self.rule_a.t4_box = "Text T4 BOX"
        self.rule_a.r1_box = "Text R1 BOX"
        self.payslip.compute_sheet()
        payslip_rule_a_line = self.payslip.line_ids.filtered(lambda p: p.salary_rule_id.id == self.rule_a.id)
        assert payslip_rule_a_line.t4_box == self.rule_a.t4_box
        assert payslip_rule_a_line.r1_box == self.rule_a.r1_box

    def test_01_assign_canadian_declaration_box(self):
        self.payslip.compute_sheet()
        self.rule_a.t4_box = "Text T4 BOX"
        self.rule_a.r1_box = "Text R1 BOX"
        self.env["hr.payslip.line"].compute_canadian_declaration()
        payslip_rule_a_line = self.payslip.line_ids.filtered(lambda p: p.salary_rule_id.id == self.rule_a.id)
        assert payslip_rule_a_line.t4_box == self.rule_a.t4_box
        assert payslip_rule_a_line.r1_box == self.rule_a.r1_box

    def test_03_compute_new_canadian_declaration_box_empty_box_only(self):
        self.rule_a.t4_box = "Text A T4 BOX"
        self.payslip.compute_sheet()
        self.rule_a.t4_box = "Text B T4 BOX"
        self.rule_a.r1_box = "Text R1 BOX"
        self.env["hr.payslip.line"].compute_canadian_declaration(replace_all=False)
        payslip_rule_a_line = self.payslip.line_ids.filtered(lambda p: p.salary_rule_id.id == self.rule_a.id)
        assert payslip_rule_a_line.r1_box == self.rule_a.r1_box
        assert payslip_rule_a_line.t4_box != self.rule_a.t4_box




from odoo.addons.hr_period.tests import test_hr_fiscalyear


class PayslipCase(test_hr_fiscalyear.TestHrFiscalyear):
    def setUp(self):
        super(PayslipCase, self).setUp()

        self.payslip_obj = self.env["hr.payslip"]
        self.run_obj = self.env["hr.payslip.run"]
        self.wzd_obj = self.env["hr.payslip.employees"]

        self.department1 = self.env["hr.department"].create({"name": "Department 1"})
        self.department2 = self.env["hr.department"].create({"name": "Department 2"})

        self.employee1 = self.env["hr.employee"].create(
            {
                "name": "Employee 1",
                "department_id": self.department1.id,
            }
        )
        self.employee2 = self.env["hr.employee"].create(
            {
                "name": "Employee 2",
                "department_id": self.department2.id,
            }
        )

    def create_contract(self, name, schedule_pay, employee, date_start):
        contract_dict = {
            "name": name,
            "employee_id": employee.id,
            "wage": 10.0,
            "schedule_pay": schedule_pay,
            "date_start": date_start,
        }
        return self.env["hr.contract"].create(contract_dict)

    def test_payslip_wizard_filters_employees_by_departments(self):
        fy = self.create_fiscal_year({"type_id": self.type_fy.id})
        fy.create_periods()
        periods = self.get_periods(fy)
        fy.button_confirm()

        date_from = periods[1].date_start
        date_to = periods[1].date_end
        contract1 = self.create_contract(
            "Contract 1", "monthly", self.employee1, date_from
        )
        contract2 = self.create_contract(
            "Contract 2", "quarterly", self.employee2, date_from
        )

        self.payslip_obj.create(
            {
                "employee_id": self.employee1.id,
                "contract_id": contract1.id,
                "date_from": date_from,
                "date_to": date_to,
                "date_payment": periods[1].date_payment,
                "company_id": self.company.id,
            }
        )
        self.payslip_obj.create(
            {
                "employee_id": self.employee2.id,
                "contract_id": contract2.id,
                "date_from": date_from,
                "date_to": date_to,
                "date_payment": periods[1].date_payment,
                "company_id": self.company.id,
            }
        )

        run = self.run_obj.create(
            {
                "name": periods[0].name,
                "date_start": periods[0].date_start,
                "date_end": periods[0].date_end,
                "date_payment": periods[0].date_payment,
                "hr_period_id": periods[0].id,
                "schedule_pay": "monthly",
                "company_id": self.company.id,
                "department_ids": [(6, 0, [self.department1.id])],
            }
        )

        wizard = run.get_payslip_employees_wizard()

        self.assertNotIn(
            self.employee1.id,
            wizard["context"]["default_employee_ids"][0][2],
            "Employee 1 should be included in the wizard.",
        )
        self.assertNotIn(
            self.employee2.id,
            wizard["context"]["default_employee_ids"][0][2],
            "Employee 2 shouldn't be included in the wizard.",
        )

        contract1.state = 'open'

        self.payslip_obj.create(
            {"employee_id": self.employee1.id, "contract_id": contract1.id,
                "date_from": date_from, "date_to": date_to,
                "date_payment": periods[1].date_payment,
                "company_id": self.company.id, })
        self.payslip_obj.create(
            {"employee_id": self.employee2.id, "contract_id": contract2.id,
                "date_from": date_from, "date_to": date_to,
                "date_payment": periods[1].date_payment,
                "company_id": self.company.id, })

        run = self.run_obj.create(
            {"name": periods[0].name, "date_start": periods[0].date_start,
                "date_end": periods[0].date_end,
                "date_payment": periods[0].date_payment, "hr_period_id": periods[0].id,
                "schedule_pay": "monthly", "company_id": self.company.id,
                "department_ids": [(6, 0, [self.department1.id])], })

        wizard = run.get_payslip_employees_wizard()

        self.assertIn(self.employee1.id,
            wizard["context"]["default_employee_ids"][0][2],
            "Employee 1 should be included in the wizard.", )



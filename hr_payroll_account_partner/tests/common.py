# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from datetime import datetime, timedelta
from odoo.tests.common import SavepointCase


class PayrollPreparationToPayslipCase(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.company = cls.env["res.company"].create({"name": "Company A"})

        cls.employee_address = cls.env["res.partner"].create(
            {"name": "My Employee's address", "type": "private",
             "employee_type": "internal"}
        )

        cls.register_address = cls.env["res.partner"].create(
            {"name": "Register address", "type": "private",
             "employee_type": "internal"}
        )

        cls.employee = cls.env["hr.employee"].create(
            {
                "name": "John Doe",
                "company_id": cls.company.id,
                "address_home_id": cls.employee_address.id,
            }
        )

        cls.register = cls.env["hr.contribution.register"].create(
            {
                "name": "Employee Register",
                "partner_id": cls.register_address.id,
            }
        )

        cls.date_start = datetime.now().date()
        cls.date_end = cls.date_start + timedelta(30)

        cls.entry_1 = cls._create_entry(cls.date_start)
        cls.entry_2 = cls._create_entry(cls.date_end)

        cls.account_debit = cls.env["account.account"].create({
            "name": "Account Debit",
            "code": 210110,
            'user_type_id': cls.env.ref(
                'account.data_account_type_payable').id,
            'reconcile': True,
        })

        cls.account_credit = cls.env["account.account"].create({
            "name": "Account Credit",
            "code": 510110,
            'user_type_id': cls.env.ref(
                'account.data_account_type_expenses').id,
            'reconcile': True,
        })

        cls.journal = cls.env["account.journal"].create(
            {
                "name": "NBC 10001 006 1000001",
                "type": "bank",
                "code": "NBC",
                "default_debit_account_id": cls.account_debit.id,
                "default_credit_account_id": cls.account_credit.id,
            }
        )

        cls.structure = cls.env.ref("hr_payroll.structure_base")
        cls.contract = cls.env["hr.contract"].create(
            {
                "name": "Test",
                "employee_id": cls.employee.id,
                "date_start": cls.date_start,
                "wage": 50000,
                "state": "open",
                "struct_id": cls.structure.id,
            }
        )

    @classmethod
    def _create_entry(cls, date_):
        return cls.env["payroll.preparation.line"].create(
            {
                "date": date_,
                "employee_id": cls.employee.id,
                "company_id": cls.company.id,
            }
        )

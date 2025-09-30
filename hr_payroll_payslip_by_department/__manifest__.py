# Copyright 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "HR Payroll Paysplip by Department",
    "version": "12.0.1.2.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Human Resources",
    "summary": "This module allows to generate payslip by department",
    "depends": ["hr_payroll", "hr_period"],
    "data": [
        "views/hr_payslip_run_views.xml",
    ],
    "installable": True,
}

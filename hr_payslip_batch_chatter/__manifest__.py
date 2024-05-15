# © 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "HR Payslip Batch Chatter",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Human Resources",
    "summary": "This module adds a chatter in payslip batch form view.",
    "depends": ["hr_payroll", "mail"],
    "data": [
        "views/hr_payslip_batch.xml",
    ],
    "installable": True,
}

# Copyright 2023 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "HR Payroll Report",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://bit.ly/numigi-com",
    "license": "AGPL-3",
    "category": "Human Resources",
    "summary": "Adds some further analysis and control features on payroll calculation lines.",
    "depends": ["payroll", "hr_payroll_period"],
    "data": [
        "views/hr_payslip_line_views.xml",
    ],
    "installable": True,
}

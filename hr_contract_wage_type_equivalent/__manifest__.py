# © 2021 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "HR Contract Wage Type Equivalent",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Human Resources",
    "summary": "Add equivalent hourly / yearly wage on contract",
    "depends": [
        "hr_contract_wage_type",
        "resource_calendar_hours_per_week",
    ],
    "data": [
        "views/hr_contract.xml",
    ],
    "installable": True,
}

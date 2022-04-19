# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "HR Employee Type Private Wizard",
    "version": "1.0.1",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Human Resources",
    "summary": "Private access to internal / external employees",
    "depends": [
        "base_view_inheritance_extension",
        "hr_employee_type",
        "hr_employee_private_wizard",
    ],
    "data": [
        "security/res_groups.xml",
        "views/hr_employee.xml",
    ],
    "installable": True,
}

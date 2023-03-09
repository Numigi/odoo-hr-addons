# © 2023 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "HR Employee Type Private Wizard",
    "version": "14.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://www.numigi.com",
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
        'security/ir.model.access.csv',
        "views/hr_employee.xml",
    ],
    "installable": True,
}

# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Payslip Chatter',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'This module adds a chatter in payslip form view.',
    'depends': ['hr_payroll', 'mail'],
    "data": [
        "views/hr_payslip.xml",
    ],
    'installable': True,
}

# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Payslip Chatter',
    'version': "14.0.1.0.0",
    'author': 'Numigi',
    'maintainer': 'Numigi',
    "website": "https://www.numigi.com",
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'This module adds a chatter in payslip form view.',
    'depends': ['hr_payroll_period', 'mail'],
    "data": [
        "views/hr_payslip.xml",
    ],
    'installable': True,
}

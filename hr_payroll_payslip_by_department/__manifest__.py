# © 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Payroll Pay Splip by Department',
    'version': '12.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'This module allows to generate payslip by department',
    'depends': ['hr_payroll'],
    'data': [
        'views/hr_payslip_run_views.xml',
    ],
    'installable': True,
}

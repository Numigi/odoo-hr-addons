# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Payroll Canadian Declaration',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'This module allows to group payslip lines by category T1 and R1',
    'depends': ['hr_payroll'],
    "data": [
        'views/hr_salary_rule.xml',
        'views/hr_payslip_line.xml',
             ],
    'installable': True,
}

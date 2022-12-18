# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Contract Wage Type',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'Distinguish between hourly / monthly / yearly wages',
    'depends': [
        'hr_contract',
    ],
    'data': [
        'views/hr_contract.xml',
    ],
    'installable': True,
}

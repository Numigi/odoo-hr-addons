# © 2018 Numigi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Main Module',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://www.numigi.com',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Install all addons required for testing.',
    'depends': [
        'hr_contract_single_open',
        'hr_contract_wage_type',  # TA#3893
        'hr_event',  # TA#3122
        'hr_working_space',  # TA#3896
        'hr_expense_same_month',  # TA#18858
    ],
    'installable': True,
}

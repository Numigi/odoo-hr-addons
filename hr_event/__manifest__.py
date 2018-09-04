# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Event',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'Add a list of events related to an employee.',
    'depends': ['hr'],
    'data': [
        'views/hr_employee.xml',
        'views/hr_event.xml',
        'views/hr_event_type.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}

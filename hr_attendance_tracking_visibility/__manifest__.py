# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Attendance Tracking Visibility',
    'version': "14.0.1.0.0",
    'author': 'Numigi',
    'maintainer': 'Numigi',
    "website": "https://www.numigi.com",
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'Enable chatter tracking for attendance changes.',
    'depends': [
        'hr_attendance',
        'hr_working_space'
    ],
    'data': [
        'views/hr_attendance.xml',
    ],
    'installable': True,
}

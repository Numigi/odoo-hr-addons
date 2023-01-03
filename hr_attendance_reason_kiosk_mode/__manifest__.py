# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Attendance Reason Kiosk Mode',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'Add Attendance Reason Using Kiosk Mode.',
    'depends': [
        'hr_attendance_reason',
    ],
    'data': [
        'views/web_asset_backend_template.xml',
    ],
    'qweb': [
        "static/src/xml/attendance.xml",
    ],
    'installable': True,
}

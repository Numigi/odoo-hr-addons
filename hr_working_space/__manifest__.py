# Copyright 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Working Space',
    'version': '16.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Specify a working space',
    'depends': [
        'hr_attendance',
    ],
    'data': [
        'views/hr_working_space.xml',
        'views/hr_attendance.xml',
        'security/ir.model.access.csv',
    ],
    "assets": {
        "web.assets_backend": [
            "hr_working_space/static/src/js/working_space_my_attendances.js",
            "hr_working_space/static/src/css/hr_working_space.css",
            "hr_working_space/static/src/xml/working_space_attendance.xml",
        ],
    },
    'installable': True,
}

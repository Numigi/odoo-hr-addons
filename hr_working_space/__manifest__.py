# -*- coding: utf-8 -*-
# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR Working Space',
    'version': '1.0.0',
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
        'views/web_asset_backend_template.xml',
    ],
    'qweb': [
        "static/src/xml/working_space_attendance.xml",
    ],
    'installable': True,
}

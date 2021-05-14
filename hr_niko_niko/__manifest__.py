# -*- coding: utf-8 -*-
# © 2021 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'HR niko niko',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'AGPL-3',
    'category': 'HR',
    'summary': 'Add niko-niko mood (check out) in attendance',
    'depends': [
        'hr_attendance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_niko_niko_data.xml',
        'views/hr_niko_niko.xml',
        'views/hr_attendance.xml',
        'views/resource_calendar.xml',
        'views/menuitem.xml',

        'views/assets.xml',
    ],
    'qweb': [
        "static/src/xml/niko_niko_attendance.xml",
    ],
    'installable': True,
}

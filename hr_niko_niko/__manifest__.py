# -*- coding: utf-8 -*-

{
    "name": "HR Niko-niko",
    "version": "1.0.0",
    "author": "Hind Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Specify a Niko-niko",
    "depends": [
        "hr_attendance",
    ],
    "data": [
        "views/hr_niko_niko.xml",
        "views/hr_attendance.xml",
        "security/ir.model.access.csv",
        "views/web_asset_backend_template.xml",
    ],
    "qweb": [
        "static/src/xml/niko_attendance.xml",
    ],
    "installable": True,
}

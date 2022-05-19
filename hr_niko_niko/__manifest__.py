# -*- coding: utf-8 -*-
{
    "name": "HR NIKO NIKO",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "MOUSSI PEE Emmanuel",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Specify employee mood Test",
    "depends": ["hr_attendance", "resource", "base_fontawesome"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_niko_views.xml",
        "views/resource_views.xml",
        "views/hr_attendance_views.xml",
        "views/hr_niko_templates.xml",
    ],
    "qweb": [
        "static/src/xml/hr_niko_attendance.xml",
    ],
    "installable": True,
}

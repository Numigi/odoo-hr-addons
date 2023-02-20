# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Hr Timesheet Attendance Report",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://bit.ly/numigi-com",
    "license": "LGPL-3",
    "category": "Human Resources",
    "summary": """Add Timesheet Report Grouped By Attendance""",
    "depends": [
        "hr_timesheet",
        "hr_attendance",
        "project_timesheet_time_control",
    ],
    "data": [
        'views/hr_timesheet_views.xml',
        'wizard/hr_timesheet_daily_time.xml'
    ],
    "installable": True,
    "post_init_hook": "recompute_attendance_hook",
}

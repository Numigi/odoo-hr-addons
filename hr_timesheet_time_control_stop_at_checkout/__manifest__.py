# © 2022 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Hr Timesheet Time Control Stop At Checkout",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://bit.ly/numigi-com",
    "license": "LGPL-3",
    "category": "Human Resources",
    "summary": """Stop a timer only when the employee leaves""",
    "depends": [
        "project_timesheet_time_control",
        "hr_attendance",
    ],
    "data": [
        "security/hr_timesheet_time_control_security.xml",
        "views/hr_timesheet_time_control_views.xml",
    ],
    "installable": True,
}

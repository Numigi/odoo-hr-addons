# © 2018 Numigi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Main Module",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://www.numigi.com",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Install all addons required for testing.",
    "depends": [
        "hr_attendance_menu_unrestricted",
        "hr_attendance_reason_kiosk_mode",  # TA#46091
        "hr_attendance_tracking_visibility",
        "hr_contract_single_open",
        "hr_contract_wage_type",
        "hr_contract_wage_type",  # TA#3893
        "hr_employee_declaration",
        "hr_employee_private_wizard",
        "hr_employee_type",  # TA#15755
        "hr_employee_type_private_wizard",
        "hr_event",  # TA#3122
        "hr_expense_same_month",  # TA#18858
        "hr_holidays_natural_period",  # TA#52493
        "hr_payroll_account_partner",
        "hr_payroll_canadian_declaration",  # TA#58633
        "hr_payroll_report",
        "hr_payslip_chatter",  # TA#24250
        "hr_working_space",  # TA#3896
        "hr_timesheet_time_control_stop_at_checkout",  # TA#46133
    ],
    "installable": True,
}

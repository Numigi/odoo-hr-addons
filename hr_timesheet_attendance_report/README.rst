Hr Timesheet Attendance Report
==============================

.. contents:: Table of Contents

Dependencies
------------

* https://github.com/OCA/project/project_timesheet_time_control

To have field `date_time` in Timesheets Lines

* https://github.com/OCA/timesheet/tree/12.0/hr_timesheet_sheet

To have Timesheets by period

Context
-------

The module allows you to have visibility on the same view of the detail of the attendance
and time entries of each employee grouped by attendance.

It adds a search icon in the Timesheet sheet to access to the daily report of time entries grouped by attendance.

Description
-----------
As member of `Timesheets / Manager`, I go to `Timesheets > Reporting > Daily Time Report`.
A new menu is added `Daily Time Report`

.. image:: static/description/daily_time_report_menu.png

Click on the menu `Daily Time Report`, a popup is shown to select the `Employee` and date to filter the list of Timesheets.
If the `Date` field is not mentioned, the report will display all periods.

.. image:: static/description/daily_time_report_popup.png

Click on `GENERATE REPORT` button to display the report.
The report is grouped by `Attendance`.
The duration is added to the group to compare it with Timesheets durations.

.. image:: static/description/daily_time_report.png


As member of `Timesheets / User`, I go to `Timesheets > My Timesheet Sheets`.

I click on an open sheet, then I can see a search icon added in the footer of `Summary` tab.

.. image:: static/description/timesheet_sheet_search_icon.png

I click on the icon of a column, I will redirected to the `Daily Time Report filtered by the selected day.

.. image:: static/description/timesheet_sheet_daily_report.png


Contributors
------------
* Numigi (tm) and all its contributors (https://bit.ly/numigiens)

More information
----------------
* Meet us at https://bit.ly/numigi-com

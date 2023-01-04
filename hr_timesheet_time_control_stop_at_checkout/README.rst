Hr Timesheet Time Control Stop At Checkout
==========================================

.. contents:: Table of Contents

Context
-------

Be able to start timers and not stop them.
When recording the exit of an employee, the current timer(s) are stopped.

This module depends of these following modules:

- `project_timesheet_time_control <https://github.com/OCA/project/tree/12.0/project_timesheet_time_control>`_
- hr_attendance

Usage
-----

New access group
~~~~~~~~~~~~~~~~

As a user who can manage user access rights, I go to the form view of a user.

I see that a new access group named Can Stop Timer is present.

.. image:: static/description/can_stop_timer_access_group.png

Hide the Stop Timer button
~~~~~~~~~~~~~~~~~~~~~~~~~~

As a `Projects and Timesheets` user, I go to the kanban view of tasks and launch a timer.

.. image:: static/description/start_timer_button.png

I notice that the Stop button is no longer available.

.. image:: static/description/stop_timer_button_hidden.png

``This behavior is the same everywhere the timer is present.``

As a user in the Can Stop Timer group, I run a timer.
I see that the Stop timer button is present.

.. image:: static/description/stop_timer_button_visible.png

Stop timer on check out
~~~~~~~~~~~~~~~~~~~~~~~

As an employee, I go to the `Attendance kiosk`, select my employee (or scan my badge) and register my entry.

.. image:: static/description/employee_check_in.png

As a `Projects and Timesheets` user, I go to the kanban view of tasks and launch a timer.

.. image:: static/description/start_task_timer.png

As an employee, I go to the `Attendance kiosk`, I select my employee (or scan my badge) and I register my exit.

.. image:: static/description/register_check_out.png

.. image:: static/description/employee_check_out.png

I see that the timer that was running on the task has been stopped and that
the duration represents the time between the start of the timer and the time of recording my check out.

.. image:: static/description/stop_timer_automatically.png

Contributors
------------
* Numigi (tm) and all its contributors (https://bit.ly/numigiens)

Employee Declarations
=====================

This module adds employee annual declaration surveys.

New Survey Type
---------------
A new survey type `Employee Declaration` is added.

.. image:: hr_employee_declaration/static/description/survey_type.png

Declarations Tab
----------------
A new tab `Declarations` is added in the employee form view.

This tab contains a few fields related to the configuration of the annual declaration.

.. image:: hr_employee_declaration/static/description/employee_declaration_tab.png

Survey
~~~~~~
This field is used to select the survey that will be sent for the declaration.
Only surveys of type `Employee Declaration` can be selected.

.. image:: hr_employee_declaration/static/description/employee_survey_field.png

Send To
~~~~~~~
This field contains the recipient of the survey.
If not filled, the survey is sent to the employee himself.

.. image:: hr_employee_declaration/static/description/employee_send_to_field.png

Periodic Declarations
~~~~~~~~~~~~~~~~~~~~~
A boolean field `Periodic Declarations` is added.

.. image:: hr_employee_declaration/static/description/employee_periodic_declaration_field.png

When checked, the following 2 fields become visible:

* Next Date: Date of the next planned declaration
* Repeat Every: Month / Year
* Declaration Email Template: Email template used to communicate the survey link to the employee.

Every night, a cron runs to send the declarations with a `Next Date` prior to the current day.
An action is scheduled in the job queue for each employeee for which the declaration must be sent.

Declaration Email Template
~~~~~~~~~~~~~~~~~~~~~~~~~~
This field is used to select the email template to use for sending the survey.

.. image:: hr_employee_declaration/static/description/employee_email_template_field.png

Here is an example of valid email for the employee declaration.

.. image:: hr_employee_declaration/static/description/mail_template_example.png

* Applies to: `Survey User Input` (survey.user_input)
* Subject: Annual Declaration for ${object.declaration_employee_id.name}
* Body:
    <p>Hello ${object.partner_id.name},</p>
    <p>Here is the link to complete the annual declaration for ${object.declaration_employee_id.name}.</p>
    <p>
    <a style="margin-left: 85px; padding:5px 10px; border-radius: 3px; background-color:#875A7B; text-align:center; color:#F7FBFD;" href="__URL__">
    Please, click here to start survey
    </a>
    </p>
    <p>Thank you</p>

The body must contain a button with `__URL__` as URL.

.. image:: hr_employee_declaration/static/description/mail_template_url_button.png

In the `Email Configuration` tab, the field `To (Partners)` must contain `${object.partner_id.id}`.

.. image:: hr_employee_declaration/static/description/mail_template_partner_to.png

Contributors
------------
* Numigi (tm) and all its contributors (https://bit.ly/numigiens)

More information
----------------
* Meet us at https://bit.ly/numigi-com

HR Payroll Canadian Declaration
===============================

Context
-------

This module allows to groub by payroll slip lines by the categories T1 and R1.

It apply the partner defined in the contribution register associated with the rule,
if it exists. Otherwise, it apply the partner associated with the employee (employee_id.address_home_id.id).

Usage
-----

1 - As a payroll user, I go to a payslip, not yet confirmed.
2 - I confirm the Payslip
3 - From the linked accounting document, I see that the partner is defined on all the lines of accounting entries.

.. image:: static/description/Account_entry_of_payslip.png


Contributors
------------
* Numigi (tm) and all its contributors (https://bit.ly/numigiens)
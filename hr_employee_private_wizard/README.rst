HR Employee Private Wizard
==========================
This module adds a wizard that allows to view and edit the private data of an employee.

Context
-------
In vanilal Odoo, either you can access a field in read/write mode, either you can not.

It is not possible to allow a user to edit a field for a subset of records that this user has access to.

This brings a limitation with sensitive HR data.
A user can either view / edit the sensitive data of all employees or no employee at all.

Module Design
-------------
This module adds a wizard.

This wizard is created from an employee record.

When the wizard is open, it shows the sensitive data of the employee.
When the wizard is saved, the sensitive data is saved to the employee.

Extending this Module
---------------------
The module contains no access validation.

Anyone with access to an employee can open and save the wizard for this employee.

Access rules should be implemented in another module to constrain
which user can view / edit the data for which employee.

Contributors
------------
* Numigi (tm) and all its contributors (https://bit.ly/numigiens)

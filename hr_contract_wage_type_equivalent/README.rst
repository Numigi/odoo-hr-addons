HR Contract Wage Type Equivalent
================================

.. contents:: Table of Contents

Context
-------
The module ``hr_contract_wage_type`` allows to select a type of wage on contracts.

The module ``resource_calendar_hours_per_week`` adds the field ``Hours Per Week`` on working schedules.

Overview
--------
This module computes equivalent hourly / yearly wage on contracts.

If an hourly wage is defined on the contract, the yearly wage is computed.

.. image:: static/description/contract_yearly_equivalent.png

Otherwise, if a yearly or a monthly wage is defined on the contract, the hourly wage is computed.

.. image:: static/description/contract_hourly_equivalent.png

The fields are computed based on the number of hours per week.

..

	Yearly Wage = Hourly Wage * Hours Per Week * 52

The number of hours per week is based on the working schedule linked to the contract.

.. image:: static/description/working_schedule.png

Contributors
------------
* Numigi (tm) and all its contributors (https://bit.ly/numigiens)

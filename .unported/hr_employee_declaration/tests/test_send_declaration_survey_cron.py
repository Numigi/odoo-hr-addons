# © 2018 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from ddt import data, ddt
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import fields
from odoo.tests import common


@ddt
class TestSendDeclarationSurveyCron(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.survey = cls.env.ref('hr_employee_declaration.demo_survey')
        cls.mail_template = cls.env.ref('hr_employee_declaration.demo_mail_template')
        cls.employee_user = cls.env['res.users'].create({
            'name': 'Employee',
            'login': 'employee',
            'email': 'employee@example.com',
        })
        cls.employee = cls.env['hr.employee'].create({
            'name': 'John Doe',
            'user_id': cls.employee_user.id,
            'periodic_declaration': True,
            'declaration_survey_id': cls.survey.id,
            'declaration_periodicity': 'month',
            'declaration_next_date': (datetime.now() - timedelta(1)).date(),
            'declaration_mail_template_id': cls.mail_template.id,
        })

    def test_afterJobIsRan_ifPeriodicityIsYear_thenNextDateIsOneYearLater(self):
        self.employee.declaration_periodicity = 'year'
        self.employee.send_declaration_survey_by_email()
        expected_date = (datetime.now() - timedelta(1) + relativedelta(years=1)).date()
        assert self.employee.declaration_next_date == expected_date

    def test_afterJobIsRan_ifPeriodicityIsMonth_thenNextDateIsOneMonthLater(self):
        self.employee.declaration_periodicity = 'month'
        self.employee.send_declaration_survey_by_email()
        expected_date = (datetime.now() - timedelta(1) + relativedelta(months=1)).date()
        assert self.employee.declaration_next_date == expected_date

    @data(
        datetime.now().date(),
        (datetime.now() - timedelta(1)).date(),
    )
    def test_ifNextDateIsTodayOrBefore_thenSendDeclaration(self, next_date):
        self.employee.declaration_next_date = next_date
        self.env['hr.employee'].send_due_declaration_surveys_by_email()
        job = self.env['queue.job'].search([
            ('model_name', '=', 'hr.employee'),
            ('method_name', '=', 'send_declaration_survey_by_email'),
        ]).filtered(lambda j: j.record_ids == [self.employee.id])
        assert len(job) == 1

    @data(
        None,
        (datetime.now() + timedelta(1)).date(),
    )
    def test_ifNextDateNotTodayOrBefore_thenDeclarationIsNotSent(self, next_date):
        self.employee.declaration_next_date = next_date
        self.env['hr.employee'].send_due_declaration_surveys_by_email()
        job = self.env['queue.job'].search([
            ('model_name', '=', 'hr.employee'),
            ('method_name', '=', 'send_declaration_survey_by_email'),
        ]).filtered(lambda j: j.record_ids == [self.employee.id])
        assert len(job) == 0

    def test_same_employee_is_not_sheduled_twice(self):
        self.employee.declaration_next_date = (datetime.now() - timedelta(1)).date()

        # Call the cron method twice
        self.env['hr.employee'].send_due_declaration_surveys_by_email()
        self.env['hr.employee'].send_due_declaration_surveys_by_email()

        job = self.env['queue.job'].search([
            ('model_name', '=', 'hr.employee'),
            ('method_name', '=', 'send_declaration_survey_by_email'),
        ]).filtered(lambda j: j.record_ids == [self.employee.id])
        assert len(job) == 1

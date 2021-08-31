# © 2018 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.exceptions import ValidationError
from odoo.tests import common


class TestSendDeclarationSurveyByEmail(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.survey = cls.env.ref('hr_employee_declaration.demo_survey')
        cls.mail_template = cls.env.ref('hr_employee_declaration.demo_mail_template')
        cls.mail_template.auto_delete = False
        cls.employee_user = cls.env['res.users'].create({
            'name': 'Employee',
            'login': 'employee',
            'email': 'employee@example.com',
        })
        cls.employee = cls.env['hr.employee'].create({
            'name': 'John Doe',
            'user_id': cls.employee_user.id,
            'declaration_survey_id': cls.survey.id,
            'declaration_mail_template_id': cls.mail_template.id,
        })
        cls.manager_user = cls.env['res.users'].create({
            'name': 'Employee',
            'login': 'manager',
            'email': 'manager@example.com',
        })
        cls.manager = cls.env['hr.employee'].create({
            'name': 'Manager',
            'user_id': cls.manager_user.id,
        })

    def test_ifSendToIsEmpty_sendSurveyToEmployee(self):
        self.employee.send_declaration_survey_by_email()
        declaration = self.employee.declaration_ids

        assert declaration.partner_id
        assert declaration.partner_id == self.employee.user_id.partner_id

    def test_ifSendToIsFilled_sendSurveyToTargetEmployee(self):
        self.employee.declaration_recipient_id = self.manager
        self.employee.send_declaration_survey_by_email()
        declaration = self.employee.declaration_ids

        assert declaration.partner_id
        assert declaration.partner_id == self.manager.user_id.partner_id

    def test_ifMailTemplateIdNotSelected_raiseValidationError(self):
        self.employee.declaration_mail_template_id = False
        with self.assertRaises(ValidationError):
            self.employee.send_declaration_survey_by_email()

    def test_ifSurveyNotSelected_raiseValidationError(self):
        self.employee.declaration_survey_id = False
        with self.assertRaises(ValidationError):
            self.employee.send_declaration_survey_by_email()

    def test_ifEmployeeHasNoUser_raiseValidationError(self):
        self.employee.user_id = False
        with self.assertRaises(ValidationError):
            self.employee.send_declaration_survey_by_email()

    def test_ifCustomRecipientHasNoUser_raiseValidationError(self):
        self.employee.declaration_recipient_id = self.manager
        self.manager.user_id = False
        with self.assertRaises(ValidationError):
            self.employee.send_declaration_survey_by_email()

    def test_token_is_added_to_email(self):
        self.employee.send_declaration_survey_by_email()

        mail = self.env['mail.mail'].search([
            ('partner_ids', '=', self.employee_user.partner_id.id),
        ], limit=1, order='id desc')

        assert self.employee.declaration_ids.token
        assert self.employee.declaration_ids.token in mail.body
        assert self.employee.declaration_ids.token in mail.body_html

    def test_mako_fields_are_converted_in_body(self):
        self.employee.send_declaration_survey_by_email()

        mail = self.env['mail.mail'].search([
            ('partner_ids', '=', self.employee_user.partner_id.id),
        ], limit=1, order='id desc')

        assert self.employee.display_name in mail.body

    def test_mako_fields_are_converted_in_subject(self):
        self.employee.declaration_recipient_id = self.manager
        self.employee.send_declaration_survey_by_email()

        mail = self.env['mail.mail'].search([
            ('partner_ids', '=', self.manager_user.partner_id.id),
        ], limit=1, order='id desc')

        assert self.manager.display_name in mail.subject

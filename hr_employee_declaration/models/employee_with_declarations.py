# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SurveyType(models.Model):

    _inherit = 'survey.type'

    is_employee_declaration = fields.Boolean()


class SurveyInputWithIsEmployeeDeclaration(models.Model):

    _inherit = 'survey.user_input'

    is_employee_declaration = fields.Boolean(
        related='survey_id.type_id.is_employee_declaration')

    declaration_employee_id = fields.Many2one(
        'hr.employee', 'Declaration Employee', ondelete='restrict')


class HrEmployeeWithDeclarations(models.Model):

    _inherit = 'hr.employee'

    declaration_ids = fields.One2many(
        'survey.user_input', string='Declarations',
        compute='_compute_declaration_ids')

    declaration_count = fields.Integer(compute='_compute_declaration_count')

    def _compute_declaration_ids(self):
        for employee in self:
            employee.declaration_ids = self.env['survey.user_input'].search([
                '|',
                ('declaration_employee_id', '=', employee.id),
                '&',
                ('declaration_employee_id', '=', False),
                ('partner_id.user_ids.employee_ids', '=', employee.id),
            ])

    def _compute_declaration_count(self):
        for employee in self:
            employee.declaration_count = len(employee.declaration_ids)

# © 2018 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SurveyUserInput(models.Model):

    _inherit = 'survey.user_input'

    is_employee_declaration = fields.Boolean(
        related='survey_id.type_id.is_employee_declaration')

    declaration_employee_id = fields.Many2one(
        'hr.employee', 'Declaration Employee', ondelete='restrict')

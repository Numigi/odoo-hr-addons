# © 2018 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SurveyType(models.Model):

    _inherit = 'survey.type'

    is_employee_declaration = fields.Boolean()

# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Employee Declarations',
    'version': '14.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'Add employee annual declarations.',
    'depends': [
        'hr',
        'queue_job',
        'survey_type',
    ],
    'data': [
        'data/survey_type.xml',
        'data/ir_cron.xml',
        'data/queue_job_function_data.xml',
        #'demo/survey.xml',
        'views/hr_employee_with_declaration_smart_button.xml',
        'views/hr_employee_with_declaration_settings.xml',
        'views/survey_type_with_is_employee_declaration.xml',
        'views/survey_user_input_with_related_employee.xml',
        'security/ir_rule.xml',
    ],
    'demo': [
        'demo/survey.xml',
    ],
    'installable': True,
}

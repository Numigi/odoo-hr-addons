# © 2022 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def recompute_attendance_hook(cr, registry):
    """ Recompute attendance of existing timesheets """
    _logger.info('Start Recomputing attendance of timesheets')
    env = api.Environment(cr, SUPERUSER_ID, {})
    model = env['account.analytic.line']
    env.add_todo(model._fields['attendance'], model.search([]))
    model.recompute()
    _logger.info('End Recomputing attendance of timesheets')

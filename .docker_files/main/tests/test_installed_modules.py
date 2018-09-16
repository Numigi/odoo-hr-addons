
from odoo.tests import TransactionCase


class TestModules(TransactionCase):
    """Test that Odoo modules are installed.

    Because some web modules have no python tests,
    we test that these modules are installed.
    """

    def setUp(self):
        super(TestModules, self).setUp()
        self.modules = self.env['ir.module.module']

    def test_hr_event(self):
        """HR Event is installed."""
        self.assertTrue(self.modules.search([('name', '=', 'hr_event')]))

    def test_hr_working_space(self):
        """Working Space is installed."""
        self.assertTrue(self.modules.search([('name', '=', 'hr_working_space')]))

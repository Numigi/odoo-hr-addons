# © 2022 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests.common import SavepointCase
from odoo.exceptions import UserError


class TestAccountAnalytic(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Customer Task",
                "email": "customer@task.com",
                "customer": True,
            }
        )

        cls.analytic_account = cls.env["account.analytic.account"].create(
            {
                "name": "My Analytic Account",
                "partner_id": cls.partner.id,
                "code": "TEST",
                "active": True,
            }
        )

        cls.analytic_account_2 = cls.env["account.analytic.account"].create(
            {
                "name": "My Analytic Account 2",
                "partner_id": cls.partner.id,
                "code": "TEST2",
                "active": True,
            }
        )

        cls.project = cls.env["project.project"].create(
            {"name": "My Project", "analytic_account_id": cls.analytic_account.id}
        )

        cls.project_2 = cls.env["project.project"].create(
            {"name": "My Project 2", "analytic_account_id": cls.analytic_account.id}
        )

        cls.task = cls.env["project.task"].create(
            {
                "name": "My Task",
                "project_id": cls.project.id,
            }
        )

        cls.analytic_line = cls.env["account.analytic.line"].create(
            {
                "name": "My Analytic line",
                "task_id": cls.task.id,
                "project_id": cls.project.id,
                "account_id": cls.analytic_account.id,
            }
        )

    def test_account_analytic_stays_active_with_timesheets(self):
        self.project_2.unlink()
        self.project.write({"active": False})
        assert self.analytic_account.active

    def test_account_analytic_stays_active_with_projects(self):
        self.analytic_line.unlink()
        self.project.write({"active": False})
        assert self.analytic_account.active

    def test_account_analytic_stays_manualy_archived_using_project_activated(self):
        self.analytic_account.toggle_active()
        self.project.write({"active": True})
        assert not self.analytic_account.active

    def test_account_analytic_archived_using_project_archived(self):
        self.project_2.unlink()
        self.analytic_line.unlink()
        self.project.write({"active": False})
        assert not self.analytic_account.active

    def test_account_analytic_active_using_project_activated(self):
        self.test_account_analytic_archived_using_project_archived()
        self.analytic_account.write({"active": True})
        assert self.analytic_account.active

    def test_not_unlink_account_if_2_projects(self):
        self.analytic_line.unlink()
        self.task.unlink()
        self.project.unlink()
        assert self.analytic_account.active

    def test_not_unlink_account_lines_unlink_project(self):
        self.project_2.unlink()
        self.task.unlink()
        self.project.unlink()
        assert len(self.analytic_account) == 1

    def test_not_change_analytic_account_project_has_timesheets(self):
        with self.assertRaises(UserError):
            self.project.analytic_account_id = self.analytic_account_2
        assert self.project.analytic_account_id & self.analytic_account

    def test_analytic_account_not_remove_project_has_timesheets(self):
        with self.assertRaises(UserError):
            self.analytic_account.project_ids = self.project_2
        assert self.analytic_account.project_ids & self.project

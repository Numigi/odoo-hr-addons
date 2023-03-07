# © 2023 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from odoo.exceptions import AccessError
from odoo.tests.common import SavepointCase


class TestPrivateWizard(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.group_internal = cls.env.ref(
            "hr_employee_type_private_wizard.group_internal"
        )
        cls.group_external = cls.env.ref(
            "hr_employee_type_private_wizard.group_external"
        )
        cls.group_private_data = cls.env.ref(
            "private_data_group.group_private_data"
        )

        cls.user = cls.env["res.users"].create(
            {
                "name": "test@example.com",
                "login": "test@example.com",
                "email": "test@example.com",
                "groups_id": [
                    (4, cls.env.ref("hr.group_hr_user").id),
                    ],
            }
        )

        cls.employee_address = cls.env["res.partner"].create(
            {"name": "My Employee's address", "type": "private", "employee_type": "internal"}
        )

        cls.employee = cls.env["hr.employee"].create(
            {
                "name": "My Employee",
                "ttype": "internal",
                "address_home_id": cls.employee_address.id,
            }
        )

        cls.employee_address = cls.employee_address.with_user(cls.user)

    def test_access_internal_employee__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.wizard = (
            self.env["hr.employee.private.wizard"]
            .with_user(self.user)
            .create({"employee_id": self.employee.id})
        )
        self.wizard.check_extended_security_all()

    def test_access_internal_employee__with_external_group(self):
        self.user.groups_id |= self.group_external
        self.wizard = (
            self.env["hr.employee.private.wizard"]
            .with_user(self.user)
            .create({"employee_id": self.employee.id})
        )
        with pytest.raises(AccessError):
            self.wizard.check_extended_security_all()

    def test_access_external_employee__with_external_group(self):
        self.user.groups_id |= self.group_external
        self.wizard = (
            self.env["hr.employee.private.wizard"]
            .with_user(self.user)
            .create({"employee_id": self.employee.id})
        )
        self.employee.ttype = "external"
        self.wizard.check_extended_security_all()

    def test_access_external_employee__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.wizard = (
            self.env["hr.employee.private.wizard"]
            .with_user(self.user)
            .create({"employee_id": self.employee.id})
        )
        self.employee.ttype = "external"
        with pytest.raises(AccessError):
            self.wizard.check_extended_security_all()

    def test_access_in_write_mode__without_write_access_to_employee(self):
        self.user.groups_id |= self.group_internal | self.group_external
        self.user.groups_id -= self.env.ref("hr.group_hr_user")
        self.wizard = (
            self.env["hr.employee.private.wizard"]
            .with_user(self.user)
            .create({"employee_id": self.employee.id})
        )
        with pytest.raises(AccessError):
            self.wizard.check_extended_security_write()

    def test_access_internal_employee_address__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.employee_address.check_extended_security_all()

    def test_access_internal_employee_address__with_external_group(self):
        self.user.groups_id |= self.group_external
        with pytest.raises(AccessError):
            self.employee_address.check_extended_security_all()

    def test_access_external_employee_address__with_external_group(self):
        self.user.groups_id |= self.group_external
        self.employee.ttype = "external"
        self.employee_address.check_extended_security_all()

    def test_access_external_employee_address__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.employee.ttype = "external"
        with pytest.raises(AccessError):
            self.employee_address.check_extended_security_all()

    def test_search_internal_employee_address__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        assert self.employee_address in self._search_partners()

    def test_search_internal_employee_address__with_external_group(self):
        self.user.groups_id |= self.group_external
        assert self.employee_address not in self._search_partners()

    def test_search_external_employee_address__with_external_group(self):
        self.user.groups_id |= self.group_external
        self.employee.ttype = "external"
        assert self.employee_address in self._search_partners()

    def test_search_external_employee_address__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.employee.ttype = "external"
        assert self.employee_address not in self._search_partners()

    def test_search_normal_partner__with_private_data_group(self):
        self.user.groups_id |= self.group_private_data
        partners = self._search_partners()
        assert self.user.partner_id in partners

    def test_search_normal_partner__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        partners = self._search_partners()
        assert self.user.partner_id in partners

    def test_search_normal_partner__with_external_group(self):
        self.user.groups_id |= self.group_external
        partners = self._search_partners()
        assert self.user.partner_id in partners

    def _search_partners(self):
        domain = self.env["res.partner"].with_user(self.user).get_extended_security_domain()
        return self.env["res.partner"].search(domain)

    def test_external_group__can_not_change_employee_type(self):
        self.user.groups_id |= self.group_external
        with pytest.raises(AccessError):
            self.employee.with_user(self.user).ttype = "external"

    def test_private_data_group__can_change_employee_type(self):
        self.user.groups_id |= self.group_private_data
        self.employee.with_user(self.user).ttype = "external"
        assert self.employee.ttype == "external"

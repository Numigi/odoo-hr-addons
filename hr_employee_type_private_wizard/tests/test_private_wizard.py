# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from odoo.exceptions import AccessError
from odoo.tests.common import SavepointCase


class TestPrivateWizard(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = cls.env["res.users"].create(
            {
                "name": "test@example.com",
                "login": "test@example.com",
                "email": "test@example.com",
                "groups_id": [(4, cls.env.ref("hr.group_hr_user").id),],
            }
        )
        cls.group_internal = cls.env.ref(
            "hr_employee_type_private_wizard.group_internal"
        )
        cls.group_external = cls.env.ref(
            "hr_employee_type_private_wizard.group_external"
        )
        cls.group_private_data = cls.env.ref(
            "private_data_group.group_private_data"
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

        cls.employee_address = cls.employee_address.sudo(cls.user)
        cls.wizard = (
            cls.env["hr.employee.private.wizard"]
            .sudo(cls.user)
            .create({"employee_id": cls.employee.id})
        )

    def test_access_internal_employee__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.wizard.check_extended_security_all()

    def test_access_internal_employee__with_external_group(self):
        self.user.groups_id |= self.group_external
        with pytest.raises(AccessError):
            self.wizard.check_extended_security_all()

    def test_access_external_employee__with_external_group(self):
        self.user.groups_id |= self.group_external
        self.employee.ttype = "external"
        self.wizard.check_extended_security_all()

    def test_access_external_employee__with_internal_group(self):
        self.user.groups_id |= self.group_internal
        self.employee.ttype = "external"
        with pytest.raises(AccessError):
            self.wizard.check_extended_security_all()

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

    def _search_partners(self):
        domain = self.env["res.partner"].sudo(self.user).get_extended_security_domain()
        return self.env["res.partner"].search(domain)

    def test_external_group__can_not_change_employee_type(self):
        self.user.groups_id |= self.group_external
        with pytest.raises(AccessError):
            self.employee.sudo(self.user).ttype = "external"

    def test_private_data_group__can_change_employee_type(self):
        self.user.groups_id |= self.group_private_data
        self.employee.sudo(self.user).ttype = "external"
        assert self.employee.ttype == "external"

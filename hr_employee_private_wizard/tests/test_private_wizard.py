# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from lxml import etree
from odoo.tests.common import SavepointCase


class TestPrivateWizard(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.gender = "female"

        cls.employee = cls.env["hr.employee"].create(
            {"name": "My Employee", "gender": cls.gender}
        )

        cls.wizard = cls.env["hr.employee.private.wizard"].create(
            {"employee_id": cls.employee.id}
        )

    def test_private_field_in_fields_view_get(self):
        result = self.wizard.fields_view_get(view_type="form")
        assert "gender" in result["fields"]

    def test_private_field_in_fields_get(self):
        fields = self.wizard.fields_get()
        assert "gender" in fields

    def test_private_field_in_fields_view_get_arch(self):
        result = self.wizard.fields_view_get(view_type="form")
        tree = result["arch"]
        field = etree.fromstring(tree).xpath("//field[@name='gender']")[0]
        assert field.attrib["modifiers"] == "{}"

    def test_public_field_in_fields_view_get_arch(self):
        result = self.wizard.fields_view_get(view_type="form")
        tree = result["arch"]
        field = etree.fromstring(tree).xpath("//field[@name='category_ids']")[0]
        assert field.attrib["modifiers"] == '{"invisible": []}'

    def test_read(self):
        data = self.wizard.read()[0]
        assert data["gender"] == self.gender

    def test_write(self):
        new_gender = "male"
        self.wizard.write({"gender": new_gender})
        assert self.employee.gender == new_gender

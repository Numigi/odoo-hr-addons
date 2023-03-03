# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from lxml import etree
from odoo import api, models, fields, _

WIZARD_FOOTER = """
    <footer>
        <button class="oe_highlight" name="save_and_close" type="object"/>
        <button name="cancel" special="cancel"/>
    </footer>
"""


class EmployeePrivateWizard(models.TransientModel):

    _name = "hr.employee.private.wizard"
    _description = "Employee Private Data Wizard"

    employee_id = fields.Many2one("hr.employee")

    def save_and_close(self):
        return {'type': 'ir.actions.act_window_close'}

    def read(self, fields=None, load="_classic_read"):
        if self._context.get("read_wizard_data"):
            return super().read(fields, load)

        res = self._get_employee().read(fields, load)
        return [dict(res[0], id=self.id)]

    def _get_employee(self):
        return (
            self.with_context(read_wizard_data=True, lang=self.env.user.lang)
            .sudo()
            .employee_id
        )

    def write(self, vals):
        self._get_employee().write(vals)
        return {"type": "ir.actions.act_window_close"}

    @api.model
    def fields_view_get(self, *args, **kwargs):
        result = (
            self.env["hr.employee"].sudo().fields_view_get(view_type="form")
        )
        tree = etree.fromstring(result["arch"])
        self._remove_non_private_arch_nodes(tree)
        _make_name_field_readonly(tree)
        _remove_image_field(tree)
        _remove_org_chart(tree)
        tree.attrib["edit"] = "0"
        tree.attrib["create"] = "0"
        tree.append(self._get_form_footer())
        result["arch"] = etree.tostring(tree)
        result["model"] = self._name
        return result

    def _get_form_footer(self):
        footer = etree.fromstring(WIZARD_FOOTER)
        buttons = footer.getchildren()
        save_button = buttons[0]
        cancel_button = buttons[1]

        if self._user_has_edit_access():
            save_button.attrib["string"] = _("Save and Close")
            cancel_button.attrib["string"] = _("Cancel")
        else:
            footer.remove(save_button)
            cancel_button.attrib["string"] = _("Close")
        return footer

    def _user_has_edit_access(self):
        employee = self._get_employee().with_user(self.env.user)
        return employee.check_access_rights("write", False)

    def _remove_non_private_arch_nodes(self, tree):
        private_fields = (
            self.env["ir.private.field"]
            .sudo()
            .search([("model_id", "=", self.env.ref("hr.model_hr_employee").id),])
        )
        field_names_to_include = set(private_fields.mapped("field_id.name"))
        field_names_to_include |= {"name"}
        _hide_child_nodes_without_fields(tree, field_names_to_include)

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        result = self.env["hr.employee"].fields_get(allfields, attributes)
        return result


def _hide_child_nodes_without_fields(tree, field_names):
    for child in tree:
        if not _has_any_field(child, field_names):
            child.attrib["modifiers"] = '{"invisible": []}'
        else:
            _hide_child_nodes_without_fields(child, field_names)


def _has_any_field(tree, field_names):
    if tree.tag == "field" and tree.attrib.get("name") in field_names:
        return True
    return any(_has_any_field(c, field_names) for c in tree)


def _make_name_field_readonly(tree):
    field = tree.xpath("//field[@name='name']")[0]
    field.attrib["modifiers"] = '{"readonly": []}'


def _remove_image_field(tree):
    _remove_node(tree, "//field[@name='image']")


def _remove_org_chart(tree):
    _remove_node(tree, "//field[@name='child_ids']")


def _remove_node(tree, xpath):
    nodes = tree.xpath(xpath)
    for node in nodes:
        node.getparent().remove(node)

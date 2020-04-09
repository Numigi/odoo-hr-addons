# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from lxml import etree
from odoo import api, models, fields


class EmployeePrivateWizard(models.TransientModel):

    _name = "hr.employee.private.wizard"
    _description = "Employee Private Data Wizard"

    employee_id = fields.Many2one("hr.employee")

    @api.multi
    def read(self, *args, **kwargs):
        if self._context.get("read_wizard_data"):
            return super().read(*args, **kwargs)

        return (
            self.with_context(read_wizard_data=True, lang=self.env.user.lang)
            .sudo()
            .employee_id.read([])
        )

    @api.multi
    def write(self, vals):
        return self.employee_id.with_context(lang=self.env.user.lang).sudo().write(vals)

    @api.model
    def fields_view_get(self, *args, **kwargs):
        view = self.env.ref("hr.view_employee_form")
        result = self.env["hr.employee"].sudo().fields_view_get(view_id=view.id)
        result["arch"] = self._remove_non_private_arch_nodes(result["arch"])
        return result

    @api.model
    def fields_get(self, *args, **kwargs):
        return self.env["hr.employee"].fields_get()

    def _remove_non_private_arch_nodes(self, arch):
        tree = etree.fromstring(arch)

        private_fields = self.env["ir.private.field"].search(
            [("model_id", "=", self.env.ref("hr.model_hr_employee").id),]
        )
        field_names_to_include = set(private_fields.mapped("field_id.name"))
        _remove_child_nodes_without_fields(tree, field_names_to_include)
        return etree.tostring(tree)


def _remove_child_nodes_without_fields(tree, field_names):
    for child in tree:
        if not _has_any_field(child, field_names):
            tree.remove(child)
        else:
            _remove_child_nodes_without_fields(child, field_names)


def _has_any_field(tree, field_names):
    if tree.tag == "field" and tree.attrib.get("name") in field_names:
        return True
    return any(_has_any_field(c, field_names) for c in tree)

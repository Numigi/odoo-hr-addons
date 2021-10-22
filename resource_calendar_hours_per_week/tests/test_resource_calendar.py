# © 2018 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.exceptions import ValidationError
from odoo.tests import common


class TestResourceCalendar(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.calendar = cls.env["resource.calendar"].create(
            {"name": "My Schedule", "attendance_ids": []}
        )

    def test_no_hours(self):
        assert self.calendar.hours_per_week == 0

    def test_one_attendance_line(self):
        self._add_attendance_line("0", 8, 12)
        assert self.calendar.hours_per_week == 4

    def test_two_attendance_lines(self):
        self._add_attendance_line("0", 8, 12)
        self._add_attendance_line("1", 8, 12)
        assert self.calendar.hours_per_week == 8

    def _add_attendance_line(self, dayofweek, hour_from, hour_to):
        vals = {
            "name": "/",
            "dayofweek": "0",
            "hour_from": 8,
            "hour_to": 12,
            "day_period": "morning",
        }
        self.calendar.write({"attendance_ids": [(0, 0, vals)]})

# Copyright 2020 Tecnativa - Víctor Martínez | Copyright 2023 - backported to v12 by Numigi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime, time

from dateutil import rrule
from pytz import timezone

from odoo import models

from odoo.addons.resource.models.resource import Intervals


class ResourceCalendar(models.Model):
    _inherit = "resource.calendar"

    def _exist_interval_in_date(self, intervals, date):
        for interval in intervals:
            if interval[0].date() == date:
                return True
        return False

    def _natural_period_intervals(self, start_dt, end_dt, interval_resource, resource):
        tz = timezone(resource.tz)
        attendances = []
        if len(interval_resource._items) > 0:
            attendances = interval_resource._items
        for day in rrule.rrule(rrule.DAILY, dtstart=start_dt, until=end_dt):
            exist_interval = self._exist_interval_in_date(
                attendances, day.date())
            if not exist_interval:
                attendances.append(
                    (
                        datetime.combine(
                            day.date(), time.min).replace(tzinfo=tz),
                        datetime.combine(
                            day.date(), time.max).replace(tzinfo=tz),
                        self.env["resource.calendar.attendance"],
                    )
                )
        return Intervals(attendances)

    def _attendance_intervals(
            self, start_dt, end_dt, resource=None):
        res = super()._attendance_intervals(
            start_dt=start_dt, end_dt=end_dt, resource=resource)
        if self.env.context.get("natural_period"):
            return self._natural_period_intervals(
                start_dt, end_dt, res, resource
            )
        return res

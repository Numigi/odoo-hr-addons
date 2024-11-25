odoo.define("hr_working_space.working_space_my_attendances", (require) => {
    "use strict";

    var core = require("web.core");
    var AttendanceWidget = require('hr_attendance.my_attendances');

    AttendanceWidget.include({
        events: _.extend({}, AttendanceWidget.prototype.events, {
            "click .o_hr_working_space_sign_in": function (event) {
                this.sign_in_with_working_space(event);
            },
        }),
        willStart() {
            var def = this._rpc({
                model: "hr.working.space",
                method: "search_read",
                fields: ["name", "icon"]
            }).then((workingSpaces) => {
                this.workingSpaces = workingSpaces;
            });
            return $.when(def, this._super.apply(this, arguments));
        },
        sign_in_with_working_space(event) {
            var workingSpaceID = event.target.id;
            this._rpc({
                model: "hr.employee",
                method: "attendance_manual_working_space",
                args: [[this.employee.id], "hr_attendance.hr_attendance_action_my_attendances", workingSpaceID]
            })
            .then((result) => {
                if (result.action) {
                    this.do_action(result.action);
                } else if (result.warning) {
                    this.do_warn(result.warning);
                }
            });
        },
    });
});

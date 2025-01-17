odoo.define("hr_working_space.working_space_my_attendances", function (require) {
    "use strict";

    var AttendanceWidget = require("hr_attendance.my_attendances");
    const session = require('web.session');

    AttendanceWidget.include({
        events: _.extend({}, AttendanceWidget.prototype.events, {
            "click .o_hr_attendance_sign_in_out_icon": _.debounce(function (event) {
                this.sign_in_with_working_space(event);
            }, 200, true),
        }),

        willStart: function () {
            var self = this;
            var def = this._rpc({
                model: "hr.working.space",
                method: "search_read",
                fields: ["name", "icon"],
                context: session.user_context,
            })
                .then(function (workingSpaces) {
                    self.workingSpaces = workingSpaces || [];
                })
                .catch(function () {
                    self.workingSpaces = [];
                    self.displayNotification({
                        title: "Error",
                        message: "Failed to fetch working spaces.",
                        type: "danger",
                    });
                });
            return Promise.all([def, this._super.apply(this, arguments)]);
        },

        sign_in_with_working_space: function (event) {
            var self = this;
            var workingSpaceID = event.currentTarget.dataset.id;
            this._rpc({
                model: "hr.employee",
                method: "attendance_manual_working_space",
                args: [
                    [self.employee.id],
                    "hr_attendance.hr_attendance_action_my_attendances",
                    workingSpaceID,
                ],
                context: session.user_context,
            })
                .then(function (result) {
                    if (result.action) {
                        self.do_action(result.action);
                    } else if (result.warning) {
                        self.displayNotification({ title: result.warning, type: "danger" });
                    }
                })
                .catch(function () {
                    self.displayNotification({
                        title: "Error",
                        message: "Failed to sign in with the selected working space.",
                        type: "danger",
                    });
                });
        },
    });

    return AttendanceWidget;
});

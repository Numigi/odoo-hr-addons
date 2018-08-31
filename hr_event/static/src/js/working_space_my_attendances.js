odoo.define("hr_working_space.working_space_my_attendances", function (require) {
    "use strict";

    var core = require("web.core");
    var Widget = require("web.Widget");

    var QWeb = core.qweb;
    var _t = core._t;


    var MyAttendancesWorkingSpace = Widget.extend({
        events: {
            "click .o_hr_working_space_sign_in_out_icon": function (event) {
                this.$(".o_hr_working_space_sign_in_out_icon").attr("disabled", "disabled");
                this.update_attendance(event);
            },
        },

        start: function () {
            var self = this;

            var def = this._rpc({
                model: "hr.employee",
                method: "search_read",
                args: [[["user_id", "=", this.getSession().uid]], ["attendance_state", "name"]],
            }).then(function (res) {
                if (_.isEmpty(res)) {
                    self.$(".o_hr_attendance_employee").append(_t("Error : Could not find employee linked to user"));
                    return;
                }
                self.employee = res[0];
            });

            var def2 = self._rpc({
                model: "hr.working.space",
                method: "search_read",
                fields: ["name", "icon"]
            }).then(function (workingSpaces) {
                self.workingSpaces = workingSpaces;
            });

            return $.when(this._super.apply(this, arguments), def, def2).done(function(){
                self.$el.html(QWeb.render("HrWorkingSpaceMyMainMenu", {widget: self}));
            });
        },

        update_attendance: function (event) {
            var self = this;
            var workingSpaceID = event.target.id;
            this._rpc({
                model: "hr.employee",
                method: "attendance_manual_working_space",
                args: [[self.employee.id], "hr_attendance.hr_attendance_action_my_attendances", workingSpaceID]
            })
                .then(function (result) {
                    if (result.action) {
                        self.do_action(result.action);
                    } else if (result.warning) {
                        self.do_warn(result.warning);
                    }
                });
        },
    });

    core.action_registry.add("hr_working_space_my_attendances", MyAttendancesWorkingSpace);

    return MyAttendancesWorkingSpace;

});
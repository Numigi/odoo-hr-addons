odoo.define("hr_niko_niko.niko_my_attendances", (require) => {
    "use strict";

    var core = require("web.core");
    var AttendanceWidget = require('hr_attendance.my_attendances');

    AttendanceWidget.include({
        events: _.extend({}, AttendanceWidget.prototype.events, {
            "click .o_hr_niko_sign_out": function (event) {
                this.sign_out_with_hr_niko_mood(event);
            },
        }),
        start() {
            var User_id = this.getSession().uid;
            var Self = [];
            var def = this._rpc({
                model: "hr.employee",
                method: "get_niko_time",
                args: [Self, User_id],
            }).then((res) => {
                this.timeniko =  res[0].nikotime;
                this.moods = res[0].moods;
            });
            return $.when(def, this._super.apply(this, arguments));
        },

        sign_out_with_hr_niko_mood(event) {
            var MoodID = event.target.id;
            this._rpc({
                model: "hr.employee",
                method: "attendance_manual_mood_id",
                args: [[this.employee.id], "hr_attendance.hr_attendance_action_my_attendances", MoodID]
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

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

            var def = this._rpc({
                model: "hr.employee",
                method: "search_read",
                fields: ['niko_time'],
                args: [[['user_id', '=', this.getSession().uid]]],
            }).then((res) => {
                console.log("niko_time..............niko_time");
                console.log(res);
                this.timeniko =  res[0].niko_time;
            });
            var def1 = this._rpc({
                model: "hr.niko",
                method: "search_read",
                fields: ["name", "icon"],
            }).then((Moods) => {
                console.log("time_niko..............time_niko");
                console.log(this.timeniko);
                if (this.timeniko) {
                    this.moods = Moods;
                } else{
                    this.moods = [];
                }
                
            });
            return $.when(def1, this._super.apply(this, arguments));
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

        get_moods() {
            this._rpc({
                model: "hr.niko",
                method: "search_read",
                fields: ["name", "icon"],
            }).then((Moods) => {
                return Moods;
            });
        },
    });
});

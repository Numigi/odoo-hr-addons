odoo.define("hr_niko_niko.niko_niko_my_attendances", (require) => {
    "use strict";

    var core = require("web.core");
    var AttendanceWidget = require('hr_attendance.my_attendances');


    AttendanceWidget.include({
        events: _.extend({}, AttendanceWidget.prototype.events, {
            "click .o_hr_niko_niko_sign_out": function (event) {
                this.sign_out_with_niko_niko(event);
            },
        }),
        start() {
            
            var def = this._rpc({
                model: "hr.niko.niko",
                method: "search_read",
                fields: ["name", "icon"]
            }).then((Nikos) => {
                this.Nikos = Nikos;
            });
            
            return $.when(def, this._super.apply(this, arguments));
        },
        
        sign_out_with_niko_niko(event) {
            var NikosID = event.target.id;
            this._rpc({
                model: "hr.employee",
                method: "attendance_manual_niko_niko",
                args: [[this.employee.id], "hr_attendance.hr_attendance_action_my_attendances", NikosID]
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

odoo.define("hr_niko_niko.my_attendances", (require) => {
    "use strict";

    var core = require("web.core");
    var QWeb = core.qweb;
    var MyAttendances = require('hr_attendance.my_attendances');

MyAttendances.include({

    start: function () {
        var self = this;

        var def = this._rpc({
                model: 'hr.employee',
                method: 'search_read',
                args: [[['user_id', '=', this.getSession().uid]], ['attendance_state', 'name', 'time_in']],
            })
            .then(function (res) {
                self.employee = res.length && res[0];
                self.$el.html(QWeb.render("HrAttendanceMyMainMenu", {widget: self}));
            });

    },


});


});

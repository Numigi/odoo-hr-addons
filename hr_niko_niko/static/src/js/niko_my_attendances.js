odoo.define("hr_niko_niko.niko_niko_my_attendances", (require) => {
    "use strict";

    var AttendanceWidget = require('hr_attendance.my_attendances');
    var core = require('web.core');
    var QWeb = core.qweb;

    function isTimeBetween(startTime, endTime, serverTime) {
        var start = moment(startTime, "H:mm")
        var end = moment(endTime, "H:mm")
        var server = moment(serverTime, "H:mm")
        if (end < start) {
            return server >= start && server <= moment('23:59:59', "h:mm:ss") || server >= moment('0:00:00', "h:mm:ss") && server < end;
        }
        return server >= start && server < end
    }

    function floatToTime(value) {
        var pattern = '%02d:%02d';
        var hour = Math.floor(value);
        var min = Math.round((value % 1) * 60);
        if (min === 60){
            min = 0;
            hour = hour + 1;
        }
        return _.str.sprintf(pattern, hour, min);
    }

    AttendanceWidget.include({
        events: _.extend({}, AttendanceWidget.prototype.events, {
            "click .o_hr_niko_niko_sign_out": function (event) {
                this.sign_out_with_niko_niko(event);
            },
        }),
        start: function () {
            var self = this;
            self.nikos = [];
            self.niko_niko = false
    
            var def = this._rpc({
                    model: 'hr.employee',
                    method: 'search_read',
                    args: [[['user_id', '=', this.getSession().uid]], ['attendance_state', 'name', "niko_niko", "niko_from", "niko_to"]],
                })
                .then(function (res) {
                    var now_time = moment.utc().local().format("HH:mm");
                    var check_niko = res[0]['niko_niko'];
                    var niko_from = res[0]['niko_from'];
                    var niko_time = floatToTime(niko_from);
                    var niko_to = res[0]['niko_to'];
                    var niko_time_to = floatToTime(niko_to);
                    if (check_niko && isTimeBetween(niko_time, niko_time_to, now_time)){
                        self._rpc({
                            model: "hr.niko.niko",
                            method: "search_read",
                            fields: ["name", "icon", "sequence"]
                            }).then(function (nikos) {
                                if (nikos.length ){
                                    nikos = nikos.sort(function(a, b){ return a.sequence - b.sequence; });
                                    self.nikos = nikos;
                                    self.niko_niko = check_niko;
                                    self.$el.html(QWeb.render("HrAttendanceMyMainMenu", {widget: self}));
                                }
                            });
                    }
                    self.employee = res.length && res[0];
                    self.$el.html(QWeb.render("HrAttendanceMyMainMenu", {widget: self}));
                });
    
            return $.when(def, this._super.apply(this, arguments));
        },

        sign_out_with_niko_niko(event) {
            var NikoNikoID = event.target.id;
            this._rpc({
                model: "hr.employee",
                method: "attendance_manual_niko",
                args: [[this.employee.id], "hr_attendance.hr_attendance_action_my_attendances", NikoNikoID]
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

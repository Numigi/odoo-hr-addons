odoo.define('hr_attendance_reason_kiosk_mode.kiosk_mode', function (require) {
"use strict";

var KioskModeWidget = require('hr_attendance.kiosk_mode');

KioskModeWidget.include({
    events: {
        "click .o_hr_attendance_button_employees": function() {
            var self = this;
            var selected_reasons = this.$el.find('.o_hr_attendance_reasons').val() || []
            var attendance_reasons = selected_reasons.map(function (x) { return parseInt(x, 10); });
            this.do_action('hr_attendance.hr_employee_attendance_action_kanban', {
                additional_context: {
                    'no_group_by': true,
                    'attendance_reasons': attendance_reasons,
                },
            });
        },
    },

    start() {
        var def = this._rpc({
            model: "hr.attendance.reason",
            method: "search_read",
            fields: ["id", "name"]
        }).then((reasons) => {
            this.attendance_reasons = reasons;
        });
        return $.when(def, this._super.apply(this, arguments));
    },
});

});

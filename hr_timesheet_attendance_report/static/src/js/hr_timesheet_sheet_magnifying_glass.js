odoo.define('hr_timesheet_attendance_report', function (require) {
    var ajax = require("web.ajax");
    var X2Many2dMatrixRenderer = require('web_widget_x2many_2d_matrix.X2Many2dMatrixRenderer');

    X2Many2dMatrixRenderer.include({

        events: {
            'click .js_generate_report': '_onClickGenerateReport',
        },

        /**
         * @override
         */

        _renderFooter: function () {
            var $footer = this._super.apply(this, arguments);
            if (this.getParent().model === 'hr_timesheet.sheet') {
                var $magnif_glass = this._renderMagnifyingGlass();
                if ($magnif_glass) {
                    var $tr = $('<tr>').append('<td/>').append($magnif_glass);
                    return $footer.append($tr);
                }
            }
            return $footer;
        },


        /**
         * @override
         */
        _renderMagnifyingGlass: function () {
            var self = this;
            return _.map(this.columns, function (column) {
                var $magnif_glass = $('<td style="align-text: center;">');
                if (column.aggregate) {
                    var $icon = $('<a href="#"><i class="fa fa-search"/>')
                    $icon.addClass('js_generate_report').attr('column', column.attrs.string)
                    $magnif_glass.append('</a>').append($icon)
                }
                return $magnif_glass;
           });
        },


        _onClickGenerateReport: function (ev) {
            ev.preventDefault();
            var self = this;
            var employee = self.state.data[0].data.employee_id.data.id
            var column = $(ev.currentTarget).attr('column')
            _.each(self.state.data, function (record) {
                if(record.data.value_x === column){
                    self.date = record.data.date
                }
            });
            return ajax.rpc("/web/action/load", {
                action_id: "hr_timesheet_attendance_report.timesheet_attendance_report_action"
                }).done(function(result) {
                    var date_from = self.date.utc().format()
                    var date_to = self.date.hours(23).minutes(59).seconds(59).utc().format()
                    result.domain = [['employee_id', '=', employee],
                                     ['date_time', '>=', date_from],
                                     ['date_time', '<=', date_to]];
                    self.getParent().do_action(result, {});
                });
        }

    });
});

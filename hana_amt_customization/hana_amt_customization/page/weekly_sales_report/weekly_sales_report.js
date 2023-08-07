frappe.pages['weekly-sales-report'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Weekly Sales Report',
		single_column: true
	});
	frappe.weekly_sales_report.make(page);
	frappe.weekly_sales_report.run();
	// let field = page.add_field({
	// 	label: 'Status',
	// 	fieldtype: 'Select',
	// 	fieldname: 'status',
	// 	options: [
	// 		'Open',
	// 		'Close'
	// 	],
	// 	change() {
			
	// 		frappe.weekly_sales_report.run(field.get_value());
	// 	}
	// });
}

frappe.weekly_sales_report = {
	start: 0,
	make: function(page) {
		var me = frappe.weekly_sales_report;
		me.page = page;
		me.body = $('<div></div>').appendTo(me.page.main);
		me.more = $('<div class="for-more"><button class="btn btn-sm btn-default btn-more">'
			+ __("More") + '</button></div>').appendTo(me.page.main)
			.find('.btn-more').on('click', function() {
				me.start += 40;
				me.run();
			});
	},
	run: function(comapny,status) {
		var me = frappe.weekly_sales_report;
		frappe.call({
			method: 'hana_amt_customization.hana_amt_customization.page.weekly_sales_report.weekly_sales_report.get_data',
			args: {
				start: me.start,
				company : comapny,
				status:status
			},
			callback: function(r) {
				if (r.message && r.message.length > 0) {
					console.log(r.message);
					r.message.forEach(function(d) {
						me.add_row(d);
					});
				} else {
					frappe.show_alert({message: __('No more updates'), indicator: 'gray'});
					me.more.parent().addClass('hidden');
				}
			}
		});
	},
	add_row: function(data) {
		var me = frappe.weekly_sales_report;
		console.log(data);
		data.by = frappe.user.full_name(data.owner);
		// data.avatar = frappe.avatar(data.sender);
		// data.when = comment_when(data.creation);

		// var date = frappe.datetime.str_to_obj(data.creation);
		// var last = me.last_feed_date;

		// if((last && frappe.datetime.obj_to_str(last) != frappe.datetime.obj_to_str(date)) || (!last)) {
		// 	var diff = frappe.datetime.get_day_diff(frappe.datetime.get_today(), frappe.datetime.obj_to_str(date));
		// 	var pdate;
		// 	if(diff < 1) {
		// 		pdate = 'Today';
		// 	} else if(diff < 2) {
		// 		pdate = 'Yesterday';
		// 	} else {
		// 		pdate = frappe.datetime.global_date_format(date);
		// 	}
			data.date_sep = data.name;
			// data.date_class = pdate=='Today' ? "date-indicator blue" : "date-indicator";
			data.date_class = "date-indicator blue";
		// } else {
		// 	data.date_sep = null;
		// 	data.date_class = "";
		// }
		// me.last_feed_date = date;

		$(frappe.render_template('weekly_sales_report_row', data)).appendTo(me.body);
		// $(frappe.render_template('team_update_row', data)).appendTo(me.body);
	},
	refresh:function(page) {
		console.log('refresh');
	}
}
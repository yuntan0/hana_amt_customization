frappe.views.calendar["Vehicle Rental Management"] = {
	field_map: {
		start: "from_date",
		end: "to_date",
		id: "name",
		allDay: "all_day",
		title: "title",
		status: "status",
		color: "color",
	},
	style_map: {
		Public: "success",
		Private: "info",
	},
	get_events_method: "hana_amt_customization.hana_amt_customization.doctype.vehicle_rental_management.vehicle_rental_management.get_events",
};

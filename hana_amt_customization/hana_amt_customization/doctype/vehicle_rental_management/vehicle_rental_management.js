// Copyright (c) 2023, John and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Rental Management', {
	refresh: function(frm) {
		if(frm.doc.status=='Booked'){
			frm.add_custom_button(__('Cancel'),function(){
				//frappe.msgprint(frm.doc.date);
				frm.doc.status = 'Cancelled';
				// frm.save();
				frappe.call({
					method: "hana_amt_customization.hana_amt_customization.doctype.vehicle_rental_management.vehicle_rental_management.cancel_car", //dotted path to server method
					args: {
						'docname':cur_frm.docname,
					},
					callback: function(r) {
						if(r.message) {
							
							frappe.msgprint('취소완료');
							frm.refresh();
							}
					}
				})
				
			},    );
			frm.add_custom_button(__('Return'),function(){
				frm.doc.status = 'Returned';
				// frm.save();
				frappe.call({
					method: "hana_amt_customization.hana_amt_customization.doctype.vehicle_rental_management.vehicle_rental_management.return_car", //dotted path to server method
					args: {
						'docname':cur_frm.docname,
					},
					callback: function(r) {
						if(r.message) {
							
							frappe.msgprint('반납완료');
							frm.refresh();
							}
					}
				})
				
			},    );
	}
	},
	onload: function(frm) {
		if(frm.doc.status=='Booked'){
			frm.add_custom_button(__('Cancel'),function(){
				frm.doc.status = 'Cancelled';
				// frm.save();
				frappe.msgprint(frm.doc.date);
				frappe.call({
					method: "hana_amt_customization.hana_amt_customization.doctype.vehicle_rental_management.vehicle_rental_management.cancel_car", //dotted path to server method
					args: {
						'docname':cur_frm.docname,
					},
					callback: function(r) {
						if(r.message) {
							
							frappe.msgprint('취소완료');
							frm.refresh();
							}
					}
				})
				
			},    );
			frm.add_custom_button(__('Return'),function(){
				frm.doc.status = 'Returned';
				// frm.save();
				frappe.call({
					method: "hana_amt_customization.hana_amt_customization.doctype.vehicle_rental_management.vehicle_rental_management.return_car", //dotted path to server method
					args: {
						'docname':cur_frm.docname,
					},
					callback: function(r) {
						if(r.message) {
							
							frappe.msgprint('반납완료');
							frm.refresh();
							}
					}
				})
				
			},    );
	}
	},
	
});

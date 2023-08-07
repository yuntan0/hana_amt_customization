# Copyright (c) 2023, John and contributors
# For license information, please see license.txt

import frappe,json
from frappe import _
from frappe.model.document import Document
from frappe.desk.reportview import get_filters_cond
from frappe.utils import (
	add_days,
	add_months,
	cint,
	cstr,
	date_diff,
	format_datetime,
	get_datetime_str,
	getdate,
	now_datetime,
	nowdate,
)
from frappe.utils.user import get_enabled_system_users
class VehicleRentalManagement(Document):
	def validate(self):
		if not self.from_date:
			self.from_date = now_datetime()

		# if start == end this scenario doesn't make sense i.e. it starts and ends at the same second!
		self.to_date = None if self.from_date == self.to_date else self.to_date

		if self.from_date and self.to_date:
			self.validate_from_to_dates("from_date", "to_date")

		if frappe.db.exists(self.doctype ,[['from_date', 'between', [self.from_date, self.to_date] ],['vehicle','=',self.vehicle],['status','=','Booked']]):
			frappe.throw(_("{0} is already booked from {1} to {2}").format(self.vehicle, self.from_date ,self.to_date))
		if frappe.db.exists(self.doctype ,[['to_date', 'between', [self.from_date, self.to_date] ],['vehicle','=',self.vehicle],['status','=','Booked']]):
			frappe.throw(_("{0} is already booked from {1} to {2}").format(self.vehicle, self.from_date ,self.to_date))


	def before_insert(self):
		self.title = "["+self.vehicle+":"+self.model+"]"+self.employee_name

		

@frappe.whitelist()
def get_events(start, end, filters=None):

	if isinstance(filters, str):
		filters = json.loads(filters)

	events = frappe.db.sql(
		"""
		SELECT name,
				employee,
				employee_name,
				color,
				from_date,
				to_date,
				all_day,
				title,
				status
		FROM `tabVehicle Rental Management`
		WHERE 1=1
		ORDER BY from_date""".format(
			
		),
		as_dict=1,
	)

	# process recurring events
	start = start.split(" ", 1)[0]
	end = end.split(" ", 1)[0]
	return events
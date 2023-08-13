import frappe

@frappe.whitelist()
def get_data(start=0,status='Open'):
	# frappe.only_for('Employee', 'System Manager')
	
	data = frappe.get_all(
		"Lead",
		fields=("name","company_name", "lead_owner",  "status",'category','annual_revenue'),
		# fields=("content", "text_content", "sender", "creation"),
		filters=dict(status=status),
		order_by="creation desc",
		limit=40,
		start=start,
	)
	for d in data:
		d.note = frappe.db.sql(
		"""
	select CONCAT('수정일시 :',tcn.modified,'<br> 노트 내용 :' ,tcn.note ) from `tabCRM Note` tcn 
		where parenttype in ('Lead' )
		and tcn.parent = %s
		order by tcn.modified desc 
		limit 1
		""",d.name ,as_dict=0)

		d.event = frappe.db.sql(
		"""
	select CONCAT('이벤트명 : ',te.subject,'<br>시작일시 :',te.starts_on,'<br> 이벤트 종류:',te.event_category,'<br>내용 : ',te.description)  as content
	from tabEvent te inner join `tabEvent Participants` tep 
	on te.name = tep.parent 
	and tep.reference_docname = %s
	and tep.reference_doctype in ('Lead') order by te.modified  desc 
		limit 1
		""",d.name ,as_dict=0)

		d.task = frappe.db.sql(
		"""
	select CONCAT('우선순위 : ',ttd.priority ,'<br>날짜 : ',ttd.`date` ,'<br>상태 : ',ttd.status ,'<br>내용 :' ,ttd.description)  from tabToDo ttd 
	where ttd.reference_type in ('Lead' )
	and ttd.reference_name =  %s
	order by ttd.modified desc limit 1
		""",d.name ,as_dict=0)
		

	# data = frappe.get_all(
	# 	"Lead",
	# 	fields=("name", "lead_name", "lead_owner", "status",'company_name','category','credit_check','annual_revenue'),
	# 	# fields=("content", "text_content", "sender", "creation"),
	# 	filters=dict(status=status),
	# 	order_by="creation desc",
	# 	limit=40,
	# 	start=start,
	# )
# 	for item in data:
# 		frappe.db.sql(
# """ 
# select CONCAT('수정일시 :',tcn.modified,'<br> 노트 내용 :' ,tcn.note ) 
# from `tabCRM Note` tcn 
# 	where parenttype in ('Opportunity' ,'Lead')
# 	and (tcn.parent = to2.name  or tcn.parent = tl.name )
# 	order by tcn.modified desc 
# 	limit 1
#  """
# 		)
# 		pass
		# item.file_url = frappe.db.get_value('File',dict(attached_to_doctype="Purchase Invoice",attached_to_name=item.name),['file_url'] ) 

	# for d in data:
	# 	d.sender_name = (
	# 		frappe.db.get_value("Employee", {"user_id": d.sender}, "employee_name") or d.sender
	# 	)
	# 	if d.text_content:
	# 		d.content = frappe.utils.md_to_html(EmailReplyParser.parse_reply(d.text_content))
	return data
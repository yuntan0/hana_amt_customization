from . import __version__ as app_version

app_name = "hana_amt_customization"
app_title = "Hana Amt Customization"
app_publisher = "John"
app_description = "Hana AMT Customization"
app_email = "yuntan0@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hana_amt_customization/css/hana_amt_customization.css"
# app_include_js = "/assets/hana_amt_customization/js/hana_amt_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/hana_amt_customization/css/hana_amt_customization.css"
# web_include_js = "/assets/hana_amt_customization/js/hana_amt_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hana_amt_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hana_amt_customization.utils.jinja_methods",
#	"filters": "hana_amt_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hana_amt_customization.install.before_install"
# after_install = "hana_amt_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hana_amt_customization.uninstall.before_uninstall"
# after_uninstall = "hana_amt_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hana_amt_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "all": [
	# 	"hana_amt_customization.tasks.all"
	# ],
	"daily": [
		"hana_amt_customization.tasks.daily"
	],
	"hourly": [
		"hana_amt_customization.tasks.hourly"
	],
	# "weekly": [
	# 	"hana_amt_customization.tasks.weekly"
	# ],
	# "monthly": [
	# 	"hana_amt_customization.tasks.monthly"
	# ],
    "cron_metal": {
		"00 14 * * *": [
			"hana_amt_customization.tasks.cron_metal"
		]
	}
}

# scheduler_events = {

# 	"all": [
# 		"common_doc.tasks.all"
# 	],
# 	"daily": [
# 		"common_doc.tasks.daily"
# 	],
# 	"hourly": [
# 		"common_doc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"common_doc.tasks.weekly"
# 	],
# 	"monthly": [
# 		"common_doc.tasks.monthly"
# 	],
# 	"cron": {
# 		"50 08 * * *": [
# 			"common_doc.tasks.cron"
# 		],
# 		"50 23 * * *": [
# 			"common_doc.tasks.cron_us"  #LA local time 08:50 KEB bank 
# 		],
# 		"30 20 * * *": [
# 			"common_doc.tasks.cron_ca"  #canada local time 16:30 bankofcanada 
# 		]
# 	}
# }

# Testing
# -------

# before_tests = "hana_amt_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "hana_amt_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hana_amt_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hana_amt_customization.auth.validate"
# ]
fixtures=[
    "Job Title", "Designation",
    "Module Profile",
    "Approval Type","Workflow","Workflow State",
    "Workflow Action Master","Translation","Identification Document Type","Expense Claim Type","Metal Code","Metal Market",
     {"dt": "Print Format", "filters": [
        [
            "name", "in", [
                "일반품의서"
            ]
        ]
    ]},
	{"dt": "Client Script", "filters": [
        [
            "module", "in", [
                "Hana Amt Customization"
            ]
        ]
    ]}

]
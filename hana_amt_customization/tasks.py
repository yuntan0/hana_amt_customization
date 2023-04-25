import frappe
import time
import json
import requests
from datetime import datetime

def all():
	pass

def daily():
	get_metal_price()

def hourly():
	get_metal_cn_price()

def weekly():
	pass

def monthly():
	pass

def cron_metal():
    get_metal_price()
    get_metal_cn_price()

# bench execute hana_amt_customization.tasks.get_metal_price
@frappe.whitelist()
def get_metal_price():
    metal_codes={'mg','cu','al'}
    for metal_code in metal_codes:
        if metal_code == 'al':
            url = "https://www.kores.net/pricetrend/baseMetalsAjax.do?mc_seq=1010004&mnrl_pc_mc_seq=495"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                for metal in res['pcdata']:
                    # print(metal)
                    metal['metal'] = 'AL'
                    metal['pc_stdr'] = res['pc_stdr']
                    metal['pc_unit_cd_n'] = res['pc_unit_cd_n']
                    metal['doctype'] = 'Metal Price'
                    print(metal)
                    if not frappe.db.exists('Metal Price',metal['metal']+"-"+metal['pc_unit_cd_n']+"-"+str(metal['pc_dt'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
        elif metal_code == 'mg':
            url = "https://www.kores.net/pricetrend/baseMetalsAjax.do?mc_seq=1020005&mnrl_pc_mc_seq=536"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                for metal in res['pcdata']:
                    # print(metal)
                    metal['metal'] = 'MG'
                    metal['pc_stdr'] = res['pc_stdr']
                    metal['pc_unit_cd_n'] = res['pc_unit_cd_n']
                    metal['doctype'] = 'Metal Price'
                    print(metal)
                    if not frappe.db.exists('Metal Price',metal['metal']+"-"+metal['pc_unit_cd_n']+"-"+str(metal['pc_dt'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
        elif metal_code == 'cu':
            url = "https://www.kores.net/pricetrend/baseMetalsAjax.do?mc_seq=1010002&mnrl_pc_mc_seq=501"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                for metal in res['pcdata']:
                    # print(metal)
                    metal['metal'] = 'CU'
                    metal['pc_stdr'] = res['pc_stdr']
                    metal['pc_unit_cd_n'] = res['pc_unit_cd_n']
                    metal['doctype'] = 'Metal Price'
                    print(metal)
                    if not frappe.db.exists('Metal Price',metal['metal']+"-"+metal['pc_unit_cd_n']+"-"+str(metal['pc_dt'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
        elif metal_code == 'ni':
            url = "https://www.kores.net/pricetrend/baseMetalsAjax.do?mc_seq=1010001&mnrl_pc_mc_seq=502"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                for metal in res['pcdata']:
                    # print(metal)
                    metal['metal'] = 'NI'
                    metal['pc_stdr'] = res['pc_stdr']
                    metal['pc_unit_cd_n'] = res['pc_unit_cd_n']
                    metal['doctype'] = 'Metal Price'
                    print(metal)
                    if not frappe.db.exists('Metal Price',metal['metal']+"-"+metal['pc_unit_cd_n']+"-"+str(metal['pc_dt'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
    

# bench execute hana_amt_customization.tasks.get_metal_cn_price
@frappe.whitelist()
def get_metal_cn_price():
    metal_codes={'al','cu','pb','zn','sn','ni'}
    
    for metal_code in metal_codes:
        if metal_code == 'al':
            url = "https://api.iyunhui.com/v2/market/price/today?metal=al"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                # print(res)
                # metal_json = json.dumps(res)
                # print(metal_json)
                for metal in res:
                    metal['metal'] = 'AL'
                    metal['doctype'] = 'Metal Price China'
                    d = datetime.fromtimestamp(int(metal['createtime']))
                    # print(d)
                    metal['createtime'] = d
                    print(metal)
                    if not frappe.db.exists('Metal Price China',metal['metal']+"-"+metal['market_name']+"-"+str(metal['createtime'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
        elif metal_code == 'cu':
            url = "https://api.iyunhui.com/v2/market/price/today?metal=cu"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                # print(res)
                # metal_json = json.dumps(res)
                # print(metal_json)
                for metal in res:
                    metal['metal'] = 'CU'
                    metal['doctype'] = 'Metal Price China'
                    d = datetime.fromtimestamp(int(metal['createtime']))
                    # print(d)
                    metal['createtime'] = d
                    print(metal)
                    if not frappe.db.exists('Metal Price China',metal['metal']+"-"+metal['market_name']+"-"+str(metal['createtime'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
        elif metal_code == 'ni':
            url = "https://api.iyunhui.com/v2/market/price/today?metal=ni"
            resp = requests.get(url)
            if (resp.status_code == 200):
                res = json.loads(resp.content)
                # print(res)
                # metal_json = json.dumps(res)
                # print(metal_json)
                for metal in res:
                    metal['metal'] = 'NI'
                    metal['doctype'] = 'Metal Price China'
                    d = datetime.fromtimestamp(int(metal['createtime']))
                    # print(d)
                    metal['createtime'] = d
                    print(metal)
                    if not frappe.db.exists('Metal Price China',metal['metal']+"-"+metal['market_name']+"-"+str(metal['createtime'])):
                        frappe.get_doc(metal).insert(
                            ignore_permissions=True
                                # ignore_permissions=True, # ignore write permissions during insert
                                # ignore_links=True, # ignore Link validation in the document
                                # ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
                                # ignore_mandatory=True # insert even if mandatory fields are not set
                        )
    
            # print(metal_price)

        # metal_doc = frappe.new_doc("Metal Price")

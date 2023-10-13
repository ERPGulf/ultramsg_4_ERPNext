# Copyright (c) 2023, ERPGulf and contributors
# For license information, please see license.txt

import frappe
# from frappe.model.document import Document
import requests
import frappe
from frappe.model.document import Document
class whatsappmessage(Document):  
 @frappe.whitelist()
 def msg(self,token, recipient,message_url,):
#    message_url=message_url
   payload = {
        'token': token,
        'to': recipient,
        'body':"This message is for testing",
       }
    
   headers = {'content-type': 'application/x-www-form-urlencoded'}

   try:
           response = requests.post(message_url, data=payload, headers=headers)
           return response.text
   except Exception as e:
          return e
   
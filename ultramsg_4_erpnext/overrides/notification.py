import frappe
from frappe import _
from frappe.email.doctype.notification.notification import Notification, get_context, json
import requests
import json

class ERPGulfNotification(Notification):
 def send(self, doc):
     
      context = get_context(doc)
      context = {"doc":doc, "alert": self, "comments": None}
      if doc.get("_comments"):
       context["comments"] = json.loads(doc.get("_comments"))
      if self.is_standard:
            self.load_standard_properties(context)
                      
      try:
           
            if self.channel == "whatsapp message":
                token = frappe.get_doc('whatsapp message').get('token')
                recipient = frappe.get_doc('whatsapp message').get('to')
                # message =self.message 
                print=self.print_format
                # frappe.msgprint(print)
                url =  frappe.get_doc('whatsapp message').get('url')
                frappe.msgprint("line26")
                self.send_ultra_whatsapp_msg(token,recipient,print,url,context)
                frappe.msgprint("line28")
                # self.whatsapp_message(doc, context)
      except:
            frappe.log_error(title='Failed to send notification', message=frappe.get_traceback())
            
      super(ERPGulfNotification, self).send(doc)
                       
 def send_ultra_whatsapp_msg(self,token,recipient,print,url,context):
    frappe.msgprint("line38")
    url=url
    # message1=frappe.render_template(self.message, context) 
    print1= frappe.render_template(self.print_format,context)
    frappe.msgprint(print1)  
    payload = {
        'token': token,
        'to': recipient,
        'body': print1,
    }
    headers = {'content-type': 'application/x-www-form-urlencoded'} 
    try:
        response = requests.post(url, data=payload, headers=headers)
        return response.text
    except Exception as e:
        return e
    

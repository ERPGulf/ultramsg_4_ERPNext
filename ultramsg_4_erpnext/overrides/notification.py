import frappe
from frappe import _
from frappe.email.doctype.notification.notification import Notification, get_context, json
import requests
import json
import io
import base64

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
                file = frappe.get_print("Print Format", "customer form", as_pdf=True)
                pdf_bytes = io.BytesIO(file)
                pdf_base64 = base64.b64encode(pdf_bytes.getvalue()).decode()
                in_memory_url = f"data:application/pdf;base64,{pdf_base64}"
                url =  frappe.get_doc('whatsapp message').get('url')
                self.send_ultra_whatsapp_msg(token,recipient,in_memory_url,url)
      except:
            frappe.log_error(title='Failed to send notification', message=frappe.get_traceback())  
      super(ERPGulfNotification, self).send(doc)
                       
 def send_ultra_whatsapp_msg(self,token,recipient,in_memory_url,url,):
    url=url
    payload = {
        'token': token,
        'to': recipient,
        "filename": "customer",
        "document": in_memory_url,
        "caption": " attached file"
    }
    headers = {'content-type': 'application/x-www-form-urlencoded'} 
    try:
        response = requests.post(url, data=payload, headers=headers)
        return response.text
    except Exception as e:
        return e
    

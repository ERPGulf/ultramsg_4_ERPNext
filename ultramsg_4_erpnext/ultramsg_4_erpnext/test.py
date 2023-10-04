import frappe
import requests
import os
import io
import base64
from pypdf import PdfWriter
from frappe.utils.pdf import get_pdf
from frappe import _
from frappe.utils.jinja import render_template
from frappe.utils import get_url
from frappe.model.document import Document
#Testing printing format to pdf using get_print
frappe.init(site ="dev.erpgulf.com",sites_path="/opt/bench3/frappe-bench/sites")
frappe.connect()
frappe.db.connect()
print("Connected to site: ", frappe.local.site)
doctype = "Sales Invoice"
docname = "ACC-SINV-2023-00006"


mypdf = frappe.get_print(doctype, docname, "Sales Invoice", as_pdf=True)
# mypdf = frappe.session.user
# Convert the PDF to bytes
pdf_bytes = io.BytesIO(mypdf)

# Encode the bytes as base64
pdf_base64 = base64.b64encode(pdf_bytes.getvalue()).decode()

# Create the in-memory URL
in_memory_url = f"data:application/pdf;base64,{pdf_base64}"

import requests
import base64

TOKEN = "imjoxycicwzpnwtj"

url = "https://api.ultramsg.com/instance63619/messages/document"

payload = {
    "token": TOKEN,
    "to": "55124924",
    "filename": "lastfile3",
    "document": in_memory_url,
    "caption": "document caption"
}

headers = {'content-type': 'application/x-www-form-urlencoded'}

# response = requests.post(url, data=payload, headers=headers)



# Check the response from the API
# print(response.text)

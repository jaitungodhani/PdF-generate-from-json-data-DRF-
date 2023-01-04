# import requests
# import json

# url = "http://127.0.0.1:8000/api/invoices/"

# payload = json.dumps({
#   "cash_in_bank": -14.61,
#   "total_current_assets": -14.61,
#   "total_assets": -14.61,
#   "net_income": 0,
#   "opening_balance_equity": -23.45,
#   "owner_loan": 576,
#   "retained_earnings": -567.16
# })
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Frame, Paragraph, Spacer, SimpleDocTemplate
# from reportlab.lib.styles import
from reportlab.lib.units import cm
from reportlab.lib import colors

pdf = SimpleDocTemplate("hello.pdf")
# pdf.translate(cm, cm)
tdata = [["name", "fname"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"]]

# doc = SimpleDocTemplate(pdf)
t = Table(tdata, colWidths=[250,250])
tstyle = TableStyle([("GRID",(0,0),(-1,-1), 1,colors.black)])
t.setStyle(tstyle)
flow_obj = []
flow_obj.append(t)
pdf.build(flow_obj)
# buffer = io.BytesIO() p = canvas.Canvas(buffer) doc = SimpleDocTemplate(p) elements = [] elements.append(Table(data)) doc.build(elements) p.showPage() p.save() buffer.seek(0)
# from django.shortcuts import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


from io import BytesIO
from rest_framework.decorators import api_view
import uuid
from datetime import date
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# @api_view(['POST'])
# def generate_balance_sheet(request, *args, **kwargs):
#     request_data = request.data

#     cash_in_bank = request_data.get("cash_in_bank", 0.00)
#     total_current_assets = request_data.get("total_current_assets", 0.00)
#     total_assets = request_data.get("total_assets", 0.00)
#     net_income = request_data.get("net_income", 0.00)
#     opening_balance_equity = request_data.get("opening_balance_equity",0.00)
#     owner_loan = request_data.get("owner_loan", 0.00)
#     retained_earnings = request_data.get("retained_earnings", 0.00)
#     today = date.today()
#     data = {
#         "cash_in_bank": cash_in_bank,
#         "total_current_assets": total_current_assets,
#         "total_assets": total_assets,
#         "net_income": net_income,
#         "opening_balance_equity": opening_balance_equity,
#         "owner_loan": owner_loan,
#         "retained_earnings" : retained_earnings,
#         "total_shareholders_equity": round(net_income + opening_balance_equity + owner_loan + retained_earnings,2),
#         "total_liabilities_and_equity" : round(net_income + opening_balance_equity + owner_loan + retained_earnings,2),
#         "date" : today.strftime("%B %d, %Y")
#     }

#     # force download
#     response = HttpResponse(content_type='application/pdf')
#     filename = "Invoice_%s.pdf" %(str(uuid.uuid4()))
#     content = "inline; filename='%s'" %(filename)
#     content = "attachment; filename=%s" %(filename)
#     response['Content-Disposition'] = content
#     template = get_template('basicapi\Balance_Sheet.html')
#     html  = template.render(data)
#     pdf = pisa.CreatePDF(html, dest=response)

#     if pdf.err:
#         return HttpResponse('we had some error <pre>' + html + '</pre>')

#     return response


@api_view(['POST'])
def generate_balance_sheet(request, *args, **kwargs):
    request_data = request.data
    today = date.today()

    cash_in_bank = request_data.get("cash_in_bank", 0.00)
    total_current_assets = request_data.get("total_current_assets", 0.00)
    total_assets = request_data.get("total_assets", 0.00)
    net_income = request_data.get("net_income", 0.00)
    opening_balance_equity = request_data.get("opening_balance_equity",0.00)
    owner_loan = request_data.get("owner_loan", 0.00)
    retained_earnings = request_data.get("retained_earnings", 0.00)
    total_shareholders_equity = round(net_income + opening_balance_equity + owner_loan + retained_earnings,2)
    total_liabilities_and_equity = round(net_income + opening_balance_equity + owner_loan + retained_earnings,2)
    today_date = today.strftime("%B %d, %Y")
    
    fileName = f"{str(uuid.uuid4())}.pdf"
    documentTitle = 'Balance Sheet'
    title = 'PBCIX'

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle(documentTitle)
    pdf.setFont("Helvetica", 18)
    pdf.drawCentredString(300, 808, title)
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(300, 785, documentTitle)
    pdf.drawCentredString(300, 770, today_date)
    pdf.line(30, 750, 550, 750)
    pdf.drawCentredString(530, 735, "TOTAL")
    pdf.line(30, 730, 550, 730)
    pdf.drawCentredString(50, 715, "Assets")
    pdf.drawCentredString(75, 700, "Current Assets")
    pdf.drawCentredString(76, 685, "Cash in bank")
    pdf.drawCentredString(530, 685, str(cash_in_bank))
    pdf.setStrokeColorRGB(0.54,0.55,0.54)
    pdf.line(30, 680, 550, 680)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(90, 665, "Total Current Assets")
    pdf.drawCentredString(530, 665, str(total_current_assets))
    pdf.line(30, 660, 550, 660)
    pdf.drawCentredString(65, 645, "Total Assets")
    pdf.drawCentredString(530, 645, str(total_assets))
    pdf.setStrokeColorRGB(0,0,0)
    pdf.line(30, 640, 550, 640)
    pdf.line(30, 637, 550, 637)
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(125, 623, "Liabilities and shareholder's equity")
    pdf.drawCentredString(95, 608, "Shareholders' equity:")
    pdf.drawCentredString(76, 595, "Net Income")
    pdf.drawCentredString(530, 595, str(net_income))
    pdf.drawCentredString(110, 580, "Opening Balance Equity")
    pdf.drawCentredString(530, 580, str(opening_balance_equity))
    pdf.drawCentredString(83, 565, "Owner's Loan")
    pdf.drawCentredString(530, 565, str(owner_loan))
    pdf.drawCentredString(95, 550, "Retained Earnings")
    pdf.drawCentredString(530, 550, str(retained_earnings))
    pdf.setFont("Helvetica-Bold", 12)
    pdf.setStrokeColorRGB(0.54,0.55,0.54)
    pdf.line(30, 545, 550, 545)
    pdf.drawCentredString(112, 530, "Total shareholders' equity")
    pdf.drawCentredString(530, 530, str(total_shareholders_equity))
    pdf.line(30, 525, 550, 525)
    pdf.drawCentredString(104, 510, "Total liabilities and equity")
    pdf.drawCentredString(530, 510, str(total_liabilities_and_equity))
    pdf.setStrokeColorRGB(0,0,0)
    pdf.line(30, 505, 550, 505)
    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=fileName)























    
    
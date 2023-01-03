from django.shortcuts import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from rest_framework.decorators import api_view
import uuid
from datetime import date

@api_view(['POST'])
def generate_invoice(request, *args, **kwargs):
    request_data = request.data

    cash_in_bank = request_data.get("cash_in_bank", 0.00)
    total_current_assets = request_data.get("total_current_assets", 0.00)
    total_assets = request_data.get("total_assets", 0.00)
    net_income = request_data.get("net_income", 0.00)
    opening_balance_equity = request_data.get("opening_balance_equity",0.00)
    owner_loan = request_data.get("owner_loan", 0.00)
    retained_earnings = request_data.get("retained_earnings", 0.00)
    today = date.today()
    data = {
        "cash_in_bank": cash_in_bank,
        "total_current_assets": total_current_assets,
        "total_assets": total_assets,
        "net_income": net_income,
        "opening_balance_equity": opening_balance_equity,
        "owner_loan": owner_loan,
        "retained_earnings" : retained_earnings,
        "total_shareholders_equity": round(net_income + opening_balance_equity + owner_loan + retained_earnings,2),
        "total_liabilities_and_equity" : round(net_income + opening_balance_equity + owner_loan + retained_earnings,2),
        "date" : today.strftime("%B %d, %Y")
    }

    # force download
    response = HttpResponse(content_type='application/pdf')
    filename = "Invoice_%s.pdf" %(str(uuid.uuid4()))
    content = "inline; filename='%s'" %(filename)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    template = get_template('basicapi/invoice.html')
    html  = template.render(data)
    pdf = pisa.CreatePDF(html, dest=response)

    if pdf.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')

    return response
    
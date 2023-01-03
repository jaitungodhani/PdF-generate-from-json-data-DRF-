from django.shortcuts import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from rest_framework.decorators import api_view
import uuid

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


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

    data = {
        "cash_in_bank": cash_in_bank,
        "total_current_assets": total_current_assets,
        "total_assets": total_assets,
        "net_income": net_income,
        "opening_balance_equity": opening_balance_equity,
        "owner_loan": owner_loan,
        "retained_earnings" : retained_earnings,
        "total_shareholders_equity": round(net_income + opening_balance_equity + owner_loan + retained_earnings,2),
        "total_liabilities_and_equity" : round(net_income + opening_balance_equity + owner_loan + retained_earnings,2)
    }
   
    pdf = render_to_pdf('basicapi/invoice.html', data)

    # force download
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %(str(uuid.uuid4()))
        content = "inline; filename='%s'" %(filename)
        content = "attachment; filename=%s" %(filename)
        print(content)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
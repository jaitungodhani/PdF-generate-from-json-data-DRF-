
from rest_framework.decorators import api_view
import uuid
from datetime import date
from django.http import FileResponse
from .pdf_generate_class import BalanceSheet

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

    buffer = BalanceSheet(cash_in_bank, total_current_assets, total_assets, net_income, opening_balance_equity, \
              owner_loan, retained_earnings, total_shareholders_equity, total_liabilities_and_equity, today_date, \
                documentTitle, title)

    return FileResponse(buffer.generate_pdf(), as_attachment=True, filename=fileName)

    























    
    
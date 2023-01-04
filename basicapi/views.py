
from rest_framework.decorators import api_view
import uuid
from datetime import date
from django.http import FileResponse
from .pdf_generate_class import BalanceSheet, ProfitandLoss, AuthorDetails
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSeriliazer

@api_view(['POST'])
def generate_balance_sheet(request, *args, **kwargs):
    try:
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
    except Exception as e:
        return Response(f"error {str(e)} is coming", status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generate_profit_and_loss_sheet(request, *args, **kwargs):
    try:
        request_data = request.data
    
        revenue_general = request_data.get("revenue_general", 0.00)
        commissions_and_fees = request_data.get("commissions_and_fees", 0.00)
        office_expenses = request_data.get("office_expenses", 0.00)
        other_selling_expenses = request_data.get("other_selling_expenses", 0.00)
        from_date = request_data.get("from_date", "1 January, 2021")
        to_date = request_data.get("to_date","2 January, 2023")
        
        fileName = f"{str(uuid.uuid4())}.pdf"
        documentTitle = 'Profit and Loss'
        title = 'PBCIX'

        buffer = ProfitandLoss(revenue_general, commissions_and_fees, office_expenses, other_selling_expenses, \
                                from_date, to_date, title, documentTitle)

        return FileResponse(buffer.generate_pdf(), as_attachment=True, filename=fileName)
    except Exception as e:
        return Response(f"error {str(e)} is coming", status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def author_details(request, pk):
    try:
        author_all_obj = Author.objects.get(pk = pk)
        serializers_data = AuthorSeriliazer(author_all_obj)
        fileName = f"{str(uuid.uuid4())}.pdf"
        documentTitle = 'Author Details'
        title = 'PBCIX'

        buffer = AuthorDetails(serializers_data.data, title, documentTitle)

        return FileResponse(buffer.main(), as_attachment=True, filename=fileName)
        
    except Exception as e:
        return Response(f"error {str(e)} is coming", status = status.HTTP_400_BAD_REQUEST)



















    
    
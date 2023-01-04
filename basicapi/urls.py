from django.urls import path
from .views import generate_balance_sheet, generate_profit_and_loss_sheet

urlpatterns = [
    path("balance_sheet/", generate_balance_sheet),
    path("profit_and_loss/", generate_profit_and_loss_sheet)
]

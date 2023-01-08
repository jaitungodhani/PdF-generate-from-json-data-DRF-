from django.urls import path
from .views import generate_balance_sheet, generate_profit_and_loss_sheet, author_details

urlpatterns = [
    path("balance_sheet/", generate_balance_sheet),
    path("profit_and_loss/", generate_profit_and_loss_sheet),
    path("author_details/", author_details)
]

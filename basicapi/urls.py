from django.urls import path
from .views import generate_balance_sheet

urlpatterns = [
    path("balance_sheet/", generate_balance_sheet)
]

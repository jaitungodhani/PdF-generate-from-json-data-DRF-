from django.urls import path
from .views import generate_invoice

urlpatterns = [
    path("invoices/", generate_invoice)
]

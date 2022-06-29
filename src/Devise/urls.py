from django.urls import path
from .views import dashboard, redirect_index

urlpatterns = [
    path("currencies=<str:currencie>&days=<int:days_rate>", dashboard, name="Dashboard"),
    path("", redirect_index, name = "redirect")
]
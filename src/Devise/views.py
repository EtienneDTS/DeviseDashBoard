from Devise.api import get_rates

from django.shortcuts import render, redirect


# Create your views here.

def redirect_index(request):
    return redirect("Dashboard", currencie="USD", days_rate=30)

def dashboard(request, currencie="USD", days_rate=30):
    currency = currencie.split(",")
    day = days_rate
    days, rates = get_rates(currencies=currency, days=day)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_rate, "personnalisé")
    return render(request, "dashboard/index.html",context={"data":rates,
                                                           "days_labels": days,
                                                           "page_label": page_label,
                                                           "currencies": currencie,
                                                           })
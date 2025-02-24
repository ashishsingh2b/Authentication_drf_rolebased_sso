from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    if request.user.is_authenticated:
        role_redirects = {
            "Customer": "customer_dashboard",
            "Engineer": "engineer_dashboard",
            "Project Manager": "pm_dashboard",
        }
        return redirect(role_redirects.get(request.user.role, "login"))
    return redirect("login")

@login_required
def customer_dashboard(request):
    return render(request, "customer_dashboard.html")

@login_required
def engineer_dashboard(request):
    return render(request, "engineer_dashboard.html")

@login_required
def pm_dashboard(request):
    return render(request, "pm_dashboard.html")
from django.shortcuts import render

def select_role(request):
    return render(request, "select_role.html")

from django.shortcuts import redirect

from django.shortcuts import redirect
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

def google_sso_redirect(request):
    role = request.GET.get('role', 'Customer')  # Default role if none is selected
    google_auth_url = reverse('social:begin', args=['google-oauth2'])  # URL for Django Social Auth
    return redirect(f"{google_auth_url}?role={role}")

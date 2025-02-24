from django.urls import path
from .views import customer_dashboard, engineer_dashboard, pm_dashboard, dashboard, google_sso_redirect,select_role
from django.contrib.auth.views import LogoutView, LoginView
from users.views import google_sso_redirect


urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('engineer_dashboard/', engineer_dashboard, name="engineer_dashboard"),
    path('customer_dashboard/', customer_dashboard, name="customer_dashboard"),
    path('pm_dashboard/', pm_dashboard, name="pm_dashboard"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sso/', google_sso_redirect, name='google_sso_redirect'),
    path('select-role/', select_role, name="select_role"),

]

from django.urls import path
from .views import *

urlpatterns = [
    path('', staff_dashboard, name="home"),

    path('staff-login/', staff_login, name="login"),
    path('staff-register/', staff_register, name="register"),
    path('staff-logout/', staff_logout, name="logout"),

    path('staff-customers/', staff_customers, name="customers"),
    path('staff-accounts/', staff_accounts, name="accounts"),
    path('staff-transactions/', staff_transactions, name="transactions"),
    path('staff-loans/', staff_loans, name="loans"),
]

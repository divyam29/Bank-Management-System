from django.urls import path
from .views import *

urlpatterns = [
    path('staff-login/', staff_login, name="login"),
    path('', staff_home, name="home"),
    path('staff-register/', staff_register, name="register"),
    path('staff-logout/', staff_logout, name="logout"),
]

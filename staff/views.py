from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def staff_home(request):
    if request.user.is_authenticated:
        return render(request, template_name='staff-dashboard.html')
    return redirect('staff:login')


def staff_login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        user=authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('staff:home')
    return render(request, template_name='staff-login.html')


def staff_register(request):
    if request.method == "POST":
        name= request.POST.get("name")
        name=name.split(" ")
        if len(name)>=0:
            fname = name[0]
            if len(name)>1:
                lname = name[1]
        email= request.POST.get("email")
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        print()
        print()
        print()
        print(fname,lname,email,uname,pwd)
        print()
        print()
        print()
        if User.objects.filter(username=uname).exists():
            return render(request, template_name='staff-register.html')
        user = User.objects.create_user(username=uname, password=pwd, email=email, first_name=fname, last_name=lname)
        user.save()
        user1 = authenticate(username=uname, password=pwd)
        if user1 is not None:
            login(request, user1)
    return render(request, template_name='staff-register.html')

def staff_logout(request):
    logout(request)
    return redirect('staff:login')
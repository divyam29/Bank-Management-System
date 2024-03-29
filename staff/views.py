from multiprocessing import context
from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.


def staff_dashboard(request):
    if request.user.is_authenticated:
        context = {
            'staff': f'{request.user.first_name} {request.user.last_name}',
        }
        return render(request, template_name='staff-dashboard.html',context=context)
    return redirect('staff:login')

def staff_customers(request):
    if request.user.is_authenticated:
        customers=Customers.objects.all()
        if request.method=='POST':
            c_name=request.POST.get('search')
            customers=Customers.objects.filter(cust_name__icontains=c_name)
        context = {
            'staff': f'{request.user.first_name} {request.user.last_name}',
            'customers':customers,
        }
        return render(request, template_name='staff-customer.html',context=context)
    return redirect('staff:login')

def staff_accounts(request):
    if request.user.is_authenticated:
        accounts=Accounts.objects.all()
        if request.method=='POST':
            c_name=request.POST.get('search')
            accounts=Accounts.objects.filter(acc_id__icontains=c_name)
        context = {
            'staff': f'{request.user.first_name} {request.user.last_name}',
            'accounts':accounts,
        }
        return render(request, template_name='staff-accounts.html',context=context)
    return redirect('staff:login')

def staff_transactions(request):
    if request.user.is_authenticated:
        transactions=Transactions.objects.all()
        if request.method=='POST':
            c_name=request.POST.get('search')
            if c_name!="":
                transactions=Transactions.objects.filter(acc_id=c_name)

        print(transactions)
        context = {
            'staff': f'{request.user.first_name} {request.user.last_name}',
            'transactions':transactions,
        }
        return render(request, template_name='staff-transaction.html',context=context)
    return redirect('staff:login')

def staff_loans(request):
    if request.user.is_authenticated:
        loans=Loans.objects.all()
        context = {
            'staff': f'{request.user.first_name} {request.user.last_name}',
            'loans':loans,
        }
        return render(request, template_name='staff-loan.html',context=context)
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
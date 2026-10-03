from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomerForm, LoanApplicationForm
from .models import LoanApplication


# Home page
def home(request):
    return render(request, 'home.html')


# Registration
def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            customer = form.save()

            # Create Django login account
            User.objects.create_user(
                username=customer.username,
                email=customer.email,
                password=customer.password
            )

            return redirect('success')

    else:
        form = CustomerForm()

    return render(request, 'register.html', {'form': form})

# Registration success
def success(request):
    return render(request, 'success.html')


# Login
def login(request):
    if request.method == 'POST':

        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        print("LOGIN VIEW CALLED")
        print("USERNAME:", repr(username))
        print("PASSWORD RECEIVED:", bool(password))

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("AUTHENTICATED USER:", user)

        if user is not None:
            auth_login(request, user)
            return redirect('Dashboard')

        return render(
            request,
            'login.html',
            {'msg': 'Invalid username and password'}
        )

    return render(request, 'login.html')

# Dashboard
def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def Dashboard(request):
    application = LoanApplication.objects.filter(
        user=request.user
    ).order_by('-applied_on').first()

    emi = None

    if application:
        emi = application.emi()

    return render(
        request,
        'dashboard.html',
        {
            'application': application,
            'emi': emi
        }
    )


# Loan Application
@login_required
def loan_application(request):
    if request.method == 'POST':

        form = LoanApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()

            return redirect('success1')

    else:
        form = LoanApplicationForm()

    return render(
        request,
        'apply_loan.html',
        {'form': form}
    )


# Application success
def success1(request):
    return render(request, 'success1.html')
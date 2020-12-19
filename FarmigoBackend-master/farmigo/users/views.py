from django.shortcuts import redirect
from django.shortcuts import render
from .forms import BaseUserCreationForm, BaseUserUpdateForm, FarmerUpdateForm, FarmerCreationForm, RetailerUpdateForm
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.contrib.auth.decorators import login_required
from django.http import *
from users.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

def test(request):
    return render(request, 'auth/test.html', {})

def home(request):
    return render(request, 'index2.html', {})

def register(request):
    form = BaseUserCreationForm()
    if request.method == 'POST':
        form = BaseUserCreationForm(request.POST)
        if form.is_valid():
            baseuser = form.save()
            if form.cleaned_data.get('user_type') == 'FMR':
                farmer = FarmerCreationForm().save(commit=False)
                farmer.baseuser = baseuser
                farmer.save()
            elif form.cleaned_data.get('user_type') == 'RTL':
                retailer = RetailerUpdateForm().save(commit=False)
                retailer.baseuser = baseuser
                retailer.save()
            return redirect('login')
        else:
            messages.error(request, f'Error Faced {form.errors}')
    else:
        form = BaseUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def profile(request):
    if request.user.user_type == "FMR":
        return render(request, 'profile/farmer.html', {})
    elif request.user.user_type == "RTL":
        return render(request, 'profile_retailer/retailer.html', {})
    elif request.user.user_type == "SPL":
        return render(request, 'profile/supplier_edit.html', {})
    else:
        messages.error(request, request.user.is_farmer)
        return render(request, 'auth/test.html', {})
# : request.user.user_type == "RTL"
@login_required
def edit_profile(request):
    if request.method == 'POST':
        base_form = BaseUserUpdateForm(request.POST, instance=request.user)
        if request.user.user_type == "FMR":
            user_form = FarmerUpdateForm(request.POST, instance=request.user.farmer)
        else:
            user_form = RetailerUpdateForm(request.POST, instance=request.user.retailer)
        
            # return render(request, 'profile/supplier_edit.html', {})
        if user_form.is_valid() and base_form.is_valid():
            user_form.save()
            base_form.save()
            messages.success(request, f'Your Profile Has Been Updated')
            return redirect('profile')
    else:
        base_form = BaseUserUpdateForm(instance=request.user)
        if request.user.user_type == "FMR":
            user_form = FarmerUpdateForm(request.POST, instance=request.user.farmer)
        elif request.user.user_type == "RTL":
            user_form = RetailerUpdateForm(request.POST, instance=request.user.retailer)
    context = {
        'form': base_form,
        'form_farmer': user_form
    }
    return render(request, 'profile/farmer_edit.html', context)



@login_required
def farmer_retailer(request):
    return render(request, 'profile/farmerRetailer.html', {})

@login_required
def farmer_supplier(request):
    return render(request, 'profile/farmerSupplier.html', {})

def weather(request):
    return render(request, 'weatherForecast.html', {})

def mandi(request):
    return render(request, 'liveMandiData.html', {})

def soil_testing(request):
    return render(request, 'soilTesting.html', {})

def blog1(request):
    return render(request, 'blogs/blog1.html', {})

def blog2(request):
    return render(request, 'blogs/blog2.html', {})
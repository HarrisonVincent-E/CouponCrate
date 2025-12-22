from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'CouponCrate/CouponCrateHome.html')

def login(request):
    return render(request, 'CouponCrate/CouponCrateLogin.html')

def successful(request):
    return render(request, 'CouponCrate/CouponCrateSuccessful.html')
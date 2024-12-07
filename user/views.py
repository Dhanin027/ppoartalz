# user/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'user/home.html')

def about_us(request):
    return render(request, 'user/about_us.html')

def services(request):
    return render(request, 'user/services.html')

def portfolio(request):
    return render(request, 'user/portfolio.html')

def blog(request):
    return render(request, 'user/blog.html')

def contact_us(request):
    return render(request, 'user/contact_us.html')

def privacy_policy(request):
    return render(request, 'user/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'user/terms_of_service.html')

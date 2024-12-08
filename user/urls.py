# user/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import contact_us
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('contact-us/', contact_us, name='contact_us'),
    path('contact-success/', TemplateView.as_view(template_name='user/contact_success.html'), name='contact_success'),
]
from django.urls import path
from .views import contact_us

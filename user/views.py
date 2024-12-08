# user/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


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

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', 'N/A')
            subject = form.cleaned_data.get('subject', 'No Subject')
            message = form.cleaned_data['message']

            # Construct the email message
            email_message = f"""
            New Contact Form Submission:
            
            Name: {name}
            Email: {email}
            Phone: {phone}
            Subject: {subject}
            
            Message:
            {message}
            """

            # Send the email
            send_mail(
                subject=f"Contact Form Submission: {subject}",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['dhanin1406@gmail.com'],  # Target email
                fail_silently=False,
            )

            # Redirect to the success page
            return redirect('contact_success')  # Redirect to a success page

    else:
        form = ContactForm()

    return render(request, 'user/contact_us.html', {'form': form})



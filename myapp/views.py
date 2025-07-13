
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def home(request):
  return render(request, 'index.html')
def about(request):
  return render(request,'about.html')
def contact(request):
  return render(request,'contact.html')
def portfolio(request):
  return render(request,'portfolio.html')
def resume(request):
  return render(request,'resume.html')
from django.core.mail import EmailMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"Message from {name} <{user_email}>:\n\n{message}"

        email = EmailMessage(
            subject=subject,
            body=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=['najiya18@gmail.com'],
            reply_to=[user_email],  # This allows you to reply to the user
        )
        email.send()
        
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('contact')

    return render(request, 'contact.html')


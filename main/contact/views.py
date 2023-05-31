import os
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from dotenv import load_dotenv

load_dotenv()

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Resume Inquiry - " + form.cleaned_data['name']
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, form.cleaned_data['email_address'], [os.environ.get('EMAIL_HOST_USER')])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "contact/message_sent.html")


    form = ContactForm()
    return render(request, "contact/contact.html", {'form':form})



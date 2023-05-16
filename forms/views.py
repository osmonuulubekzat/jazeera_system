from django.shortcuts import render, redirect
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def Index(request):
    return render(request, "index.html")


def Message(request):
    return render(request, "message.html")


def Forms(request):
    if request.method == "POST":
        FirsName = request.POST["name"]
        LastName = request.POST["lastname"]
        PhoneNumber = request.POST["phone"]
        Email = request.POST["email"]
        region = request.POST["region"]
        clint_list = OurСlints.objects.all()
        email_list = list(OurСlints.objects.values_list("Email", flat=True))
        if Email not in email_list:
            contact = OurСlints.objects.create(FirstName=FirsName, LastName=LastName, PhoneNumber=PhoneNumber,
                                               Email=Email, Region=region)
            contact.save()
            return redirect("message")
        else:
            return redirect("index")

    else:

        return render(request, 'forms.html')

def SendMessage(request):
    mydict = {'username': "Bekzat Osmon uulu "}
    html_template = 'email_message.html'
    html_message = render_to_string(html_template, context=mydict)
    subject = 'Welcome to Service-Verse'
    email_from = settings.EMAIL_HOST_USER
    resivers = list(OurСlints.objects.values_list("Email", flat=True))
    recipient_list = resivers
    message = EmailMessage(subject, html_message,
                           email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
    return redirect("index")




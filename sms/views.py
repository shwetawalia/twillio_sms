from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from twilio.rest import Client
from django.conf import settings
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import loader

def home(request):
    
    if request.method == "POST":
        phone = request.POST.get('phone', '')
        confirm_message = "Message sent successfully."    
        to =  phone
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        response = client.messages.create(
            body=loader.render_to_string('temp.html'),
            to=to, from_=settings.TWILIO_PHONE_NUMBER)
        return render(request, 'index.html', {'confirm_message': confirm_message})
   
    
    
    return render(request, 'index.html')
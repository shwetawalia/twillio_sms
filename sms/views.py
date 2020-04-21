from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from twilio.rest import Client
from django.conf import settings

def home(request):
    '''
        uncomment phone make code dynamic and any no. get from form will get the meassage
    '''
    if request.method == "POST":
        phone = request.POST.get('phone', '')
        confirm_message = "Message sent successfully."    
        to =  phone
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        response = client.messages.create(
            body='Hello testing twilio in Django',
            to=to, from_=settings.TWILIO_PHONE_NUMBER)
        return render(request, 'index.html', {'confirm_message': confirm_message})
   
    
    
    return render(request, 'index.html')


from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def elements(request):
    return render(request, "elements.html")

def dishend(request):
    return render(request, "Dishend.html")

def generic(request):
    return render(request, "generic.html")

def hemi(request):
    return render(request, "Hemi spherical.html")

def infra(request):
    return render(request, "Infrastructure.html")

def inspection(request):
    return render(request, "Inspection.html")

def photogallery(request):
    return render(request, "photogallery.html")

def pipecaps(request):
    return render(request, "Pipecaps.html")

def quality(request):
    return render(request, "Quality.html")

def tori(request):
    return render(request, "Tori.html")

def ourclients(request):
    return render(request, "OurClients.html")

def chatbot(request):
    return render(request, "chatbot.html")

from django.http import JsonResponse

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient, sender_email, sender_password):
    # Create message object instance
    message = MIMEMultipart()

    # Set the message body
    message.attach(MIMEText(body, 'plain'))

    # Set the message subject
    message['Subject'] = subject

    # Set the message recipient
    message['To'] = recipient

    # Set the message sender
    message['From'] = sender_email

    # Connect to the SMTP server and send the message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient, message.as_string())
    server.quit()

def chatbot_response(request):
    user_input = request.GET.get('user_input', '').lower()
    print(request.GET.get('hi_done',''))
    hi_done = request.GET.get('hi_done','') == 'true'
    specifications = request.GET.get('specifications', '').lower()

    if user_input == 'hi':
        response = {'response': 'Hello! Enter your specifications.',
                    'hi_done':"true",
                    'specifications':specifications}
        return JsonResponse(response)
    
    if hi_done:
        
        if 'yes' in user_input:
            response = {'response': 'Specifications noted.',
                    'hi_done':"true",
                    'specifications':specifications}
            send_email("User Specifications", specifications, "19bce062@nirmauni.ac.in", "19bce062@nirmauni.ac.in", "oegpmovihbpdvmev")
            return JsonResponse(response)
        
        elif 'no' in user_input:
            specifications = ""
            response = {'response': 'Enter your specification again.',
                    'hi_done':"true",
                    'specifications':specifications}
            return JsonResponse(response)
        
        else:
            specifications = user_input
            response = {'response': f'Is this your specification? "{user_input}"',
                    'hi_done':"true",
                    'specifications':specifications}
            return JsonResponse(response)

    else:
        response = {'response': 'I did not understand.',
                    'hi_done':"false",
                    'specifications':specifications}
        return JsonResponse(response)


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



def fnc_for_name(all_vars):
    if 'yes' in all_vars["user_input"]:
        all_vars["name_enterd"] = "true"
        all_vars["response"] = ["Name noted. Now enter your company name."]
    
    elif 'no' in all_vars["user_input"]:
        all_vars["response"] = ["Enter you name again"]
    
    else:
        all_vars["response"] = [f"Is {all_vars['user_input']} your correct name?"]
        all_vars["user_name"] = all_vars['user_input']
    return all_vars

def fnc_for_company(all_vars):
    if 'yes' in all_vars["user_input"]:
        all_vars["company_enterd"] = "true"
        all_vars["response"] = ["company noted. Now enter your phone number."]
    
    elif 'no' in all_vars["user_input"]:
        all_vars["response"] = ["Enter you company name again"]
    
    else:
        all_vars["response"] = [f"Is {all_vars['user_input']} your correct name of your company?"]
        all_vars["user_company"] = all_vars['user_input']
    return all_vars

def fnc_for_phone(all_vars):
    if 'yes' in all_vars["user_input"]:
        all_vars["phone_enterd"] = "true"
        all_vars["response"] = ["Phone Number noted. Now product type."]
    
    elif 'no' in all_vars["user_input"]:
        all_vars["response"] = ["Enter you phone number again"]
    
    else:
        all_vars["response"] = [f"Is {all_vars['user_input']} your correct phone number?"]
        all_vars["user_phone"] = all_vars['user_input']
    return all_vars



def chatbot_response(request):
    user_input = request.GET.get('user_input', '').lower()
    hi_done = request.GET.get('hi_done','')
    specifications = request.GET.get('specifications', '').lower()
    name_enterd = request.GET.get('name_enterd', '').lower()
    user_name = request.GET.get('user_name', '').lower()
    company_enterd = request.GET.get('company_enterd', '').lower()
    user_company = request.GET.get('user_company', '').lower()
    phone_enterd = request.GET.get('phone_enterd', '').lower()
    user_phone = request.GET.get('user_phone', '').lower()


    all_vars = {'response': [''],
                'user_input': user_input,
                'hi_done':hi_done,
                'specifications':specifications,
                "name_enterd":name_enterd,
                'user_name':user_name,
                "company_enterd":company_enterd,
                'user_company':user_company,
                "phone_enterd":phone_enterd,
                'user_phone':user_phone}

    if all_vars["user_input"] == 'hi':
        all_vars['response'] = ['Hello!', 'Please Enter your name.']
        all_vars['hi_done'] = "true"
        all_vars['specifications'] = ""
        all_vars['name_enterd'] = "false"
        all_vars['user_name'] = ""
        all_vars['company_enterd'] = "false"
        all_vars['user_company'] = ""
        all_vars['phone_enterd'] = "false"
        all_vars['user_phone'] = ""
        return JsonResponse(all_vars)
    
    if all_vars["hi_done"] == "true":

        print(all_vars["name_enterd"])

        if all_vars["name_enterd"] == "true":
            if all_vars["company_enterd"] == "true":

                if all_vars['phone_enterd'] == "true":
                    all_vars["response"] = ["Everything noted!"]
                else:
                    all_vars=fnc_for_phone(all_vars)
            else:
                all_vars = fnc_for_company(all_vars)
            
        
        else:
            all_vars = fnc_for_name(all_vars)
        
        # if 'yes' in user_input:
        #     response = {'response': 'Specifications noted.',
        #             'hi_done':"true",
        #             'specifications':specifications}
        #     send_email("User Specifications", specifications, "steel.fit123@gmail.com", "steel.fit123@gmail.com", "bndknnudyeshzodt")
        #     send_email("User Specifications", specifications, "dwijmakvana@gmail.com", "steel.fit123@gmail.com", "bndknnudyeshzodt")
        #     return JsonResponse(response)
        
        # elif 'no' in user_input:
        #     specifications = ""
        #     response = {'response': 'Enter your specification again.',
        #             'hi_done':"true",
        #             'specifications':specifications}
        #     return JsonResponse(response)
        
        # else:
        #     specifications = user_input
        #     response = {'response': f'Is this your specification? "{user_input}"',
        #             'hi_done':"true",
        #             'specifications':specifications}
        #     return JsonResponse(response)

    else:
        all_vars["response"] = ["please type hi to start the conversation"]

    return JsonResponse(all_vars)


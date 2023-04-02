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

def chatbot_response(request):
    user_input = request.GET.get('user_input', '').lower()
    hi_done = request.GET.get('hi_done','') == 'true'

    if user_input == 'hi':
        response = {'response': 'Hello! Enter your specifications.',
                    'hi_done':"true"}
        return JsonResponse(response)
    
    if hi_done:
        
        if 'yes' in user_input:
            response = {'response': 'Specifications noted.',
                    'hi_done':"true"}
            return JsonResponse(response)
        
        elif 'no' in user_input:
            response = {'response': 'Enter your specification again.',
                    'hi_done':"true"}
            return JsonResponse(response)
        
        else:
            response = {'response': f'Is this your specification? "{user_input}"',
                    'hi_done':"true"}
            return JsonResponse(response)

    else:
        response = {'response': 'I did not understand.',
                    'hi_done':"false"}
        return JsonResponse(response)


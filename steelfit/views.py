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
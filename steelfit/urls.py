from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('infrastructure/', infrastructure, name='infrastructure'),
    path('certificates/', certificates, name='certificates'),
    path('clients/', clients, name='clients'),
    path('contact/', contact, name='contact'),
    path('dishend/', dishend, name='dishend'),
    path('pipecap/', pipecap, name='pipecap'),
    path('cones/', cones, name='cones'),
    path('chatbot/',chatbot,name='chatbot'),
    path('chatbot-response/', chatbot_response, name='chatbot_response')
]
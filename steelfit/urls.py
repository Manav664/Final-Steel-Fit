from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('elements/', elements, name='elements'),
    path('dishend/', dishend, name='dishend'),
    path('generic/', generic, name='generic'),
    path('hemi_spherical/', hemi, name='hemi'),
    path('infrastructure/', infra, name='infra'),
    path('inspection/', inspection, name='inspection'),
    path('photogallery/', photogallery, name='photogallery'),
    path('pipecaps/', pipecaps, name='pipecaps'),
    path('quality/', quality, name='quality'),
    path('tori/', tori, name='tori'),
]
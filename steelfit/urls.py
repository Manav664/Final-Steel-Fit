from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('elements/', elements),
    path('dishend/', dishend),
    path('generic/', generic),
    path('hemi_spherical/', hemi),
    path('infrastructure/', infra),
    path('inspection/', inspection),
    path('photogallery/', photogallery),
    path('pipecaps/', pipecaps),
    path('quality/', quality),
    path('tori/', tori),
]
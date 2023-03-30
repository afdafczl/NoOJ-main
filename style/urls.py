from django.urls import path
from style.views import *

urlpatterns = [
    path('',index),
    path('submitpage/',submitpage),
    path('submit/',submit),
]


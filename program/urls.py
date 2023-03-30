from django.urls import path
from program.views import *

urlpatterns = [
    path('index/',index),
    path('cre_program/',cre_program),
    path('query_program/', query_program),
    path('cre_test/', cre_test),
    path('query_test/', query_test),
    #path('submitpage/',submitpage),
    #path('submit/',submit),
]


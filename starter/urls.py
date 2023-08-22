from django.urls import path
from . import views

urlpatterns=[
    path("",views.landing,name="index"),
    path("message/send",views.send_message,name="send_message"),
]
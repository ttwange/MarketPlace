from django.urls import path
from . import views


app_name = 'core'
urlspatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name="contact")
]
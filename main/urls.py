
from django.urls import path

from main import views

app_name="main"

urlpatterns = [
    path('',views.home, name='Home'),
    path('about',views.about, name='About'),
    path('contact',views.contact, name='Contact')
]
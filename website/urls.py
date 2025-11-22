from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
]
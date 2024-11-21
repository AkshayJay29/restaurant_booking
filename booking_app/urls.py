from django.urls import path
from . import views

app_name = 'booking_app'  # Namespace for the app

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
]

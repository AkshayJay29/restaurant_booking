from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
]

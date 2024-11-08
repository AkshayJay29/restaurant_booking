from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import MenuItem, Booking
from .forms import BookingForm

def index(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')
    return render(request, 'booking_app/index.html', {'form': form})

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'booking_app/menu.html', {'items': items})

def booking_confirmation(request):
    return render(request, 'booking_app/booking_confirmation.html')


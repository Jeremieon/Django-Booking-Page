from django.shortcuts import render
from .forms import InputForm,BookingForm
from .models import Booking
# Create your views here.
def index(request):
    booking_data = Booking.objects.all()
    context = {'book_data' : booking_data}
    return render(request,'user_form/index.html',context)

def forms_meth(request):
    context = {'form':InputForm}
    return render(request,'user_form/form.html',context)
   # return render(request,'user_app/index.html',context)
def my_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            booking_date = form.cleaned_data.get('booking_date')
            form.save()
            return render(request,'user_form/form.html')
    else:
        form = BookingForm()
    booking_data = Booking.objects.all()
    context = {'booking' : BookingForm,
              'book_data' : booking_data
        }
    return render(request,'user_form/form.html',context)



from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from NinazHairline.forms import SubscribeForm


# Create your views here.

services = [
    {'id': 1, 'name':'Buy Hairs Here!'},
    {'id': 2, 'name':'Book MakeUp Services!'},
    {'id': 3, 'name':'Book Haircut Services!'},
    {'id': 4, 'name':'Book Braiding Services!'},
]

def home(request):
    context = {'services': services}
    return render(request, 'NinazHairline/home.html', context)

def dashboard(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Welcome Onboard'
            message = 'Thanks for subscribing to our news feed.\nWe will keep you posted and updated the whole time of the way.\nHosted by Johnson Masino(Back End Developer.)'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Successfully Sent!')
            return redirect('dashboard')
    return render(request, 'NinazHairline/dashboard.html', {'form': form})




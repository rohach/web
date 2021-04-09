from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import json
import datetime
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from .models import Room
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


@login_required()
def home(request):

    return render(request, 'user/home.html')

@login_required()
def experiences(request):
    return render(request, 'experiences.html')

@login_required()
def impact(request):
    return render(request, 'impact.html')

@login_required()
def about(request):
    return render(request, 'about.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def first(request):
    return render(request, 'user/first.html')


class AddBookingView(CreateView):
    model = Room
    template_name = 'addBooking.html'
    fields = '__all__'
    success_url = reverse_lazy('booking')

@login_required()
def BookingView(request):

    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'booking.html', context)


class RoomView(DetailView):
    model = Room
    template_name = 'view.html'

class RoomUpdate(UpdateView):
    model = Room
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('booking')


class RoomDelete(DeleteView):
    model = Room
    template_name = 'delete.html'
    success_url = reverse_lazy('booking')





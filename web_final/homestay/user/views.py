
from django.shortcuts import render



def home(request):

    return render(request, 'user/home.html')


def experiences(request):
    return render(request, 'experiences.html')


def impact(request):
    return render(request, 'impact.html')


def about(request):
    return render(request, 'about.html')
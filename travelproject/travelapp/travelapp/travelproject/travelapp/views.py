# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

# Create your views here.


def demo(request):
    place=Place.objects.all()

    return render(request, 'index.html',{'result':place})


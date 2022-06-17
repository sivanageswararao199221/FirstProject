from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1><marquee> THIS IS MY FIRST FBV</marquee></h1>')

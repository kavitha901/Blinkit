from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def diry(request):
    return HttpResponse('<h1><marquee>Dairy products are fresh in blinkit</marquee></h1>')

def kv(request):
    return render(request,'kv.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def groc(request):
    return HttpResponse('<h1><marquee>Groceries are available in blinkit</marquee></h1>')

def ku(request):
    return render(request,'ku.html')
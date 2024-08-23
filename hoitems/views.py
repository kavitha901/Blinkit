from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def items(request):
    return HttpResponse('<h1>Home and Office items are cheap in blinkit</h1>')

def dk(request):
    return render(request,'dk.html')
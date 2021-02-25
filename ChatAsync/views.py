# chat/views.py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ChatAsync/index.html')

def room(request,room_name):
    context={
        'room_name':room_name,
    }
    return render(request,template_name='ChatAsync/room.html',context=context)


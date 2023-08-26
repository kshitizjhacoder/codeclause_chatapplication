from django.shortcuts import render
from .models import Message
def index(request):
    return render(request, 'index.html')

def chat_room(request,room_name):
    username = request.GET.get('username','Anonymous')
    messages = Message.objects.filter(room = room_name)[0:25]
    return render(request, 'chat_room.html',{'username':username,'room_name':room_name,'messages':messages})

from django.shortcuts import render


def index(request):
    return render(request,'chat_app/index.html',{}) 

def chat_room(request,room_name):
    return render(request,'chat_app/chatroom.html',{'room_name':room_name}) 
    
# Create your views here.

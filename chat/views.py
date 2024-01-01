from django.shortcuts import render
from .models import Message , ChatRoom

def chatbox(request , chat_box_name):
    user_data = Message.objects.all()
    chat_room = Message.objects.select_related('chatid')
    return render(request,'chat/chat.html', {"chat_box_name": chat_box_name , 'user_data':user_data , 'chat_room':chat_room})
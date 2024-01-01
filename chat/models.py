from django.db import models
from users.models import Users

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=500)

class Message(models.Model):
    message_text = models.TextField()
    userid = models.ForeignKey(Users , on_delete=models.CASCADE)
    chatid = models.ForeignKey(ChatRoom , on_delete=models.CASCADE)
    def __str__(self):
        return self.message_text
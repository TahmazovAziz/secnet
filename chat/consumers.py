import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from users.models import Users
from .models import Message , ChatRoom

class RoomChat(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope['url_route']['kwargs']['chat_box_name']
        self.group_name = "chat_%s" % self.chat_box_name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        username_content = text_data_json['username']
        chat_record = await sync_to_async(ChatRoom.objects.filter(room_name=self.group_name).first)()
        if chat_record is not None:
            chat_name = chat_record
        else:
            chat_name = await sync_to_async(ChatRoom.objects.create)(room_name=self.group_name)
        
        username = await sync_to_async(Users.objects.get)(username=username_content)
        message = await sync_to_async(Message.objects.create)(message_text=message_content , userid=username ,chatid=chat_name)

        await self.channel_layer.group_send(
            
            self.group_name,
            {
                "type":"chatbox_message",
                "message":message_content,
                "username":username_content,
            }
        )

    async def chatbox_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(
            text_data=json.dumps(
                {
                    "message":message,
                    "username":username
                }
            )
        )



import pytest
from django.test import TestCase
from asgiref.sync import sync_to_async
from channels.routing import URLRouter
from channels.testing import WebsocketCommunicator
from chat.consumers import RoomChat
from socnet.routing import websocket_urlpatterns
from users.models import Users
@pytest.mark.asyncio
class ChannelsTest(TestCase):
    # async def setUp(self):
    #     user = await sync_to_async(Users.objects.create)(username='root')        
    async def test_consumer(self):
        try:          
            user = await sync_to_async(Users.objects.get)(username='user')
            comunicator = WebsocketCommunicator(URLRouter(websocket_urlpatterns), "ws/chat/chat_box_name/")
            connected , _ = await comunicator.connect()
            await comunicator.send_json_to({"type":"chat.message","username":'user',"message":"Hello World!"})
            response = await comunicator.receive_json_from()
            assert response["type"] == "chat.message"
            assert response["username"] == 'user'
            assert response["message"] == "Hello World!"
            await comunicator.disconnect()

        except Users.DoesNotExist:
            print('dont find user')
            


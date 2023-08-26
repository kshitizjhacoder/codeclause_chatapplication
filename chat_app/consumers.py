import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s'%self.room_name
        await self.channel_layer.group_add(
            self.room_group_name
            ,self.channel_name
        )
        print("message+username")
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self,text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        roomname = data['room']
        await self.save_message(username,roomname,message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message,
                'username':username,
            }
        )
        print(message+' '+username)

    
    async def chat_message(self,event):
        message = event['message']
        username = event['username']
        print(message+username)
        await self.send(text_data=json.dumps({'message': message,'username':username}))

    @sync_to_async
    def save_message(self,username,room,message):
        Message.objects.create(username = username,room = room,message = message)

# import json

# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s'%self.room_name 
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name  
#         )
#         self.accept()

#         # self.send(text_data=json.dumps({
#         #     'type':'connection_established',
#         #     'message':'You are now connected',
#         # }))

#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type':'chat_message',
#                 'message': message
#             }
#         )
#         print('Message', message)
#         # You can implement the chat logic here. For simplicity, we'll just echo the message back.
#         # self.send(text_data=json.dumps({'type':'chat','message': message}))
#     def chat_message(self,event):
#         message = event['message']
#         self.send(text_data=json.dumps({'type':'chat','message': message}))
# ChatAsync/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('async')
        print(type(self))
        print('channel_name',self.channel_name)
        print('channel_layer',self.channel_layer)
        print('channel_layer_alias',self.channel_layer_alias)
        print('channel_receive',self.channel_receive)
        print('groups',self.groups)
        print('base_send',self.base_send)
        #print('__slots__',self.__slots__)
        #print('dict',self.__dict__)

        for i in self.scope:
            print(i,self.scope[i])
        


        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print('async','accepted')
        await self.send(text_data=json.dumps({
            'message': 'conection accepted'
        }))

    async def disconnect(self, close_code):
        print('async','disconnected')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #with out channels
    # def receive(self, text_data):
    #     print(text_data)

    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))

    # Receive message from WebSocket
    async def receive(self, text_data):
        # print('text_data',text_data)
        # print(type(self))
        # print('channel_name',self.channel_name)
        # print('channel_layer',self.channel_layer)
        # print('channel_layer_alias',self.channel_layer_alias)
        # print('channel_receive',self.channel_receive)
        # print('groups',self.groups)
        # print('base_send',self.base_send)
        # #print('__slots__',self.__slots__)
        # print('dict',self.__dict__)

        # for i in self.scope:
        #     print(i,self.scope[i])

        # Send message to room group
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        #print('got message ',message)
        print('async','got message',message)
        print('async','sending to group',self.room_group_name)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        #print('message_evnt',event)
        #print('channel_name',self.channel_name)
        message = event['message']
        print('async','send message',message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
# ChatAsync/consumers.py
import json
from datetime import datetime 
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class OcppConsumer(AsyncWebsocketConsumer):
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
        print('dict',self.__dict__)

        for i in self.scope:
            print(i,self.scope[i])


        await self.accept('ocpp1.6')

        #print('scope method',self.scope["method"])
        


        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = 'chat_%s' % self.room_name
        
        # # Join room group
        # await self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )
        # await self.accept()
        # print('async','accepted')
        # await self.send(text_data=json.dumps({
        #     'message': 'conection accepted'
        # }))

    async def disconnect(self, close_code):
        print('async','disconnected')
        print('close_code',close_code)
        # await self.channel_layer.group_discard(
        #     self.room_group_name,
        #     self.channel_name
        # )

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
        print(text_data_json)
        message_type=text_data_json[0]
        message_id=text_data_json[1]
        message_opration=text_data_json[2]
        message_payload=text_data_json[3]
        
        for i in message_payload:
            print(i)
        if message_opration=="BootNotification":
            res_payload={}
            res_payload['status']="Accepted"
            res_payload['currentTime']=datetime.now().isoformat()
            res_payload['interval']=14400
            j_res=[3,message_id,res_payload]
            await self.send(text_data=json.dumps(j_res))    


    # Receive message from room group
    async def chat_message(self, event):
        print('inside chat message')
        print('message_evnt',event)
        print('channel_name',self.channel_name)
        message = event['message']
        print('async','send message',message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
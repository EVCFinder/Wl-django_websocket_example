# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):

        print(type(self))
        print("channel_name", self.channel_name)
        print("channel_layer", self.channel_layer)
        print("channel_layer_alias", self.channel_layer_alias)
        print("channel_receive", self.channel_receive)
        print("groups", self.groups)
        print("base_send", self.base_send)
        # print('__slots__',self.__slots__)
        # print('dict',self.__dict__)

        for i in self.scope:
            print(i, self.scope[i])

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"message": "conection accepted"}))
        self.chat_message(
            event={
                "type": "chat.message",
                "message": "message from consumer by suing channel layer",
            }
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # with out channels
    # def receive(self, text_data):
    #     print(text_data)

    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))

    # Receive message from WebSocket
    def receive(self, text_data):
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
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        print("inside chat message ")
        print("message_evnt", event)
        print("channel_name", self.channel_name)
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

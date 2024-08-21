import json
from channels.generic.websocket import AsyncWebsocketConsumer

from colorama import Fore, Back, Style
from datetime import datetime

def print_log(status, whoami, api, message) :
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    if status == "active" :
        print("\n-----------------------------------------\n"   + 
              current_time + " [ " + whoami + " ] send to : " +Fore.BLUE + "[ " + api + " ]\n" +  Fore.RESET +
              Fore.GREEN + "[active] " + Fore.RESET + "message: [ " + Fore.GREEN + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")
    elif status == "error" :
        print("\n-----------------------------------------\n"   + 
              current_time + " " + whoami + Fore.BLUE + "[ " + api + " ]\n" +  Fore.RESET +
              Fore.RED + "[error] " + Fore.RESET + "message: [ " + Fore.RED + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")

i_am_api_wno = 'Router API - WNO'

class AEYE_WL_consumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()


    async def disconnect(self, close_code):
        # 그룹에서 탈퇴
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        print_log('active', i_am_api_wno, i_am_api_wno, "Client Sent to WS {}".format(text_data))

        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '')
            # 메시지를 처리하는 로직 추가
            await self.send(text_data=json.dumps({
                'message': message
            }))
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'error': 'Invalid JSON format'
            }))

    async def chat_message(self, event):
        message = event['message']

        # WebSocket에 메시지 보내기
        await self.send(text_data=json.dumps({
            'message': message
        }))
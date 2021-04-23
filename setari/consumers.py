from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep
from channels.exceptions import StopConsumer
from jokes.tasks import get_joke1, get_joke2


class WSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        ok = get_joke1.delay().get()
        await self.send(json.dumps({'message': ok}))
        print("Client is connected!")
        
    async def disconnect(self, close_code):
        print('disconnected! ', close_code)
        raise StopConsumer()


class WSConsumer2(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        ok = get_joke2.delay().get()
        await self.send(json.dumps({'message': ok}))
        print("Alt Client is connected!")
        
    async def disconnect(self, close_code):
        print('disconnected! ', close_code)
        raise StopConsumer()

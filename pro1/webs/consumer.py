

from channels.generic.websocket import AsyncWebsocketConsumer

class PiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            'pi_group',
            {
                'type': 'pi_message',
                'data': text_data
            }
        )

    async def pi_message(self, event):
        data = event['data']
        await self.send(text_data=data)

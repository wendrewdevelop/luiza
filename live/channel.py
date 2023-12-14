import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Aqui você pode processar os dados se estiverem em formato de texto
        pass

    async def receive_bytes(self, bytes_data):
        # Aqui você processa os dados se estiverem em formato de bytes
        # bytes_data contém os dados do frame em bytes (imagem, por exemplo)

        # Adapte a lógica conforme necessário
        # Neste exemplo, enviamos os bytes para todos os clientes conectados
        await self.send_bytes(bytes_data)
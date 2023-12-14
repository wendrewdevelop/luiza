from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from luiza.utils import convert_frame_to_jpeg


class StreamAPI(APIView):
    def post(self, request):
        channel_layer = get_channel_layer()

        # Lógica para receber frames (assumindo que os frames estão em um formato de imagem)
        frame = request.data.get('frame', None)

        if frame:
            # Converte o frame para o formato JPEG
            frame_jpeg = convert_frame_to_jpeg(frame)

            # Envia o frame para todos os clientes WebSocket conectados
            async_to_sync(channel_layer.group_send)(
                'livestream_group',
                {
                    'type': 'send_frame',
                    'frame': frame_jpeg,
                }
            )

            return Response({'message': 'Frame recebido e enviado com sucesso.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Frame não recebido.'}, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import aeye_wlh_models
from .serializers import aeye_wlh_serializers
from colorama import Fore, Back, Style
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import aiohttp

i_am_api_wlh = 'Router API - WLH'

class aeye_wlh_Viewsets(viewsets.ModelViewSet):
    queryset=aeye_wlh_models.objects.all().order_by('id')
    serializer_class=aeye_wlh_serializers

    def create(self, request) :
        serializer = aeye_wlh_serializers(data = request.data)

        if serializer.is_valid() :
            i_am_client      = serializer.validated_data.get('whoami')
            message_client   = serializer.validated_data.get('message')

            # WebSocket을 통해 데이터를 전송합니다.
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'data_channel',
                {
                    'whoami' : i_am_api_wlh,
                    'message': message_client
                }
            )
            message="Succeed to print by WebSocket"
            data={
                'whoami' : i_am_api_wlh,
                'message': message
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            pass


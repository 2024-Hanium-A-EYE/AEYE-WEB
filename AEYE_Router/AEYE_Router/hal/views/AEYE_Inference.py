from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import aeye_inference_models
from .serializers import aeye_inference_serializers
from colorama import Fore, Back, Style
from datetime import datetime
import requests
import os

def print_log(status, whoami, hal, message) :
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    if status == "active" :
        print("\n-----------------------------------------\n"   + 
              current_time + " [ " + whoami + " ] send to : " + Fore.BLUE + "[ " + hal + " ]\n" +  Fore.RESET +
              Fore.GREEN + "[active] " + Fore.RESET + "message: [ " + Fore.GREEN + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")
    elif status == "error" :
        print("\n-----------------------------------------\n"   + 
              current_time + " [ " + whoami + " ] send to : " + "[ " + hal + " ]\n" +  Fore.RESET +
              Fore.RED + "[error] " + Fore.RESET + "message: [ " + Fore.RED + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")

i_am_hal_infer = 'Router HAL - Inference'

server_url='http://13.209.24.64:3000/'
api_ano='api/ai-network-operator/'

class aeye_inference_Viewswets(viewsets.ModelViewSet):
    queryset=aeye_inference_models.objects.all().order_by('id')
    serializer_class=aeye_inference_serializers

    def create(self, request) :
        serializer = aeye_inference_serializers(data = request.data)

        if serializer.is_valid() :
            i_am_client    = serializer.validated_data.get('whoami')
            message_client = serializer.validated_data.get('message')
            print_log('active', i_am_client, i_am_hal_infer, "Succeed to Received Data : {}".format(message_client))

            image_client = request.FILES.get('image')
            url='{}{}'.format(server_url, api_ano)
            response_server = aeye_ai_inference_request(image_client, url)
            
            if response_server.status_code == 200:
                server_data = response_server.json()
                
                i_am_server    = server_data.get('whoami')
                message_server = server_data.get('message')
                ai_result      = server_data.get('ai_result')
                gpt_result     = server_data.get('gpt_result')
                
                message = "Succed to Receive Data from : {}".format(url)
                print_log('active', i_am_server, i_am_hal_infer, message)
               
                data={
                    'whoami'     : i_am_hal_infer,
                    'message'    : message,
                    'ai_result'  : ai_result,
                    'gpt_result' : gpt_result
                }

                return Response(data, status=status.HTTP_200_OK)
            else:
                message="Failed to Receive Data from : {}".format(url)
                print_log('error', i_am_hal_infer, i_am_hal_infer, message)
                data={
                    'whoami' : i_am_hal_infer,
                    'message': message
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = "Client Sent Invalid Data : {}".format(serializer.errors)
            print_log('error', i_am_hal_infer, i_am_hal_infer, message)
            data={
                'whoami' : i_am_hal_infer,
                'message': message
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



def aeye_ai_inference_request(image, url)->str:

    files = {
            'image': (image.name, image.read(), image.content_type),
    }

    data = {
        'whoami' : i_am_hal_infer,
        'operation' : 'Inference',
        'message' : 'Request AI Inference',
    }
    print_log('active', i_am_hal_infer, i_am_hal_infer, "Send Data to : {}".format(url))
    response = requests.post(url, data=data, files=files)
    return response

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import aeye_database_read_models, aeye_database_list_models
from .serializers import aeye_database_read_serializers, aeye_database_list_serializers
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

i_am_hal_read_data = 'Router HAL - DataBase Read'

server_url=''
api_ano=''

class aeye_database_read_Viewswets(viewsets.ModelViewSet):
    queryset = aeye_database_list_models.objects.all()
    serializer_class = aeye_database_list_serializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
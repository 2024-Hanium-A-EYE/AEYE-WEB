from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import aeye_database_read_list_models, aeye_database_patient_models
from .serializers import aeye_read_list_serializers, aeye_patient_serializers

from colorama import Fore, Back, Style
from datetime import datetime

def print_log(status, whoami, hal, message) :
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    if status == "active" :
        print("\n-----------------------------------------\n"   + 
              current_time + " [ " + whoami + " ] send to : " + Fore.BLUE + "[ " + hal + " ]\n" +  Fore.RESET +
              Fore.GREEN + "[active] " + Fore.RESET + "message: [ " + Fore.GREEN + str(message) +" ]" + Fore.RESET +
              "\n-----------------------------------------")
    elif status == "error" :
        print("\n-----------------------------------------\n"   + 
              current_time + " [ " + whoami + " ] send to : " + "[ " + hal + " ]\n" +  Fore.RESET +
              Fore.RED + "[error] " + Fore.RESET + "message: [ " + Fore.RED + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")

i_am_hal_read_data_list = 'Router HAL - DataBase Read List'


class aeye_database_read_list_ViewSet(viewsets.ModelViewSet):
    queryset = aeye_database_read_list_models.objects.all()
    serializer_class = aeye_read_list_serializers

    def create(self, request) :
        serializer = aeye_read_list_serializers(data=request.data)        
        message="Requested to Read Database by ID"
        print_log('active', i_am_hal_read_data_list, i_am_hal_read_data_list, message)
        
        if serializer.is_valid():
                
            try:
                patient = aeye_database_patient_models.objects.all()
                print_log('active', i_am_hal_read_data_list, i_am_hal_read_data_list, patient)
                serializer = aeye_patient_serializers(patient, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except aeye_database_patient_models.DoesNotExist:
                message = "Patient not found"
                data={
                    'whoami' : i_am_hal_read_data_list,
                    'message': message
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            message="{}".format(serializer.errors)
            data={
                'whoami' : i_am_hal_read_data_list,
                'message': message
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        

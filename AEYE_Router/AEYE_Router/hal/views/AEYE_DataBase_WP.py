from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import aeye_database_patient_models
from .serializers import aeye_patient_serializer

from colorama import Fore, Back, Style
from datetime import datetime

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

i_am_hal_write_data_patient = 'Router HAL - DataBase Write Patient'


class aeye_database_patient_ViewSet(viewsets.ModelViewSet):
    queryset = aeye_database_patient_models.objects.all()
    serializer_class = aeye_patient_serializer
    
    def create(self, request) :
        serializer = aeye_patient_serializer(data = request.data)

        if serializer.is_valid() :
            message="Client Requested DataBase Write Patient"
            print_log('active', i_am_hal_write_data_patient, i_am_hal_write_data_patient, message)
            serializer.save()

            data={
                'whoami' : i_am_hal_write_data_patient,
                'message': "Succed to Save Patient"
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            message="{}".format(serializer.errors)
            print_log('error', i_am_hal_write_data_patient, i_am_hal_write_data_patient, message)
            data={
                'whoami' : i_am_hal_write_data_patient,
                'message': message
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

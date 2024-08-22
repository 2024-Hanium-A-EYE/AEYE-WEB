from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import aeye_database_read_detail_models, aeye_database_patient_models
from .serializers import aeye_read_deatil_serializers, aeye_patient_serializers

from colorama import Fore, Back, Style
from datetime import datetime

def print_log(status, whoami, hal, message):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    if status == "active":
        print("\n-----------------------------------------\n" +
              current_time + " [ " + whoami + " ] send to : " + Fore.BLUE + "[ " + hal + " ]\n" + Fore.RESET +
              Fore.GREEN + "[active] " + Fore.RESET + "message: [ " + Fore.GREEN + str(message) + " ]" + Fore.RESET +
              "\n-----------------------------------------")
    elif status == "error":
        print("\n-----------------------------------------\n" +
              current_time + " [ " + whoami + " ] send to : " + "[ " + hal + " ]\n" + Fore.RESET +
              Fore.RED + "[error] " + Fore.RESET + "message: [ " + Fore.RED + message + " ]" + Fore.RESET +
              "\n-----------------------------------------")

i_am_hal_read_data_detail = 'Router HAL - DataBase Read Detail'


class aeye_database_read_detail_ViewSet(viewsets.ViewSet):

    queryset = aeye_database_read_detail_models.objects.all() 
    serializer_class = aeye_read_deatil_serializers

    def retrieve(self, request, pk=None):
        message = "Requested to Read Database by ID"
        print_log('active', i_am_hal_read_data_detail, i_am_hal_read_data_detail, message)
        
        try:
            # pk를 사용하여 Patient 객체를 가져옴
            patient = aeye_database_patient_models.objects.get(id=pk)
            serializer = aeye_patient_serializers(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except aeye_database_patient_models.DoesNotExist:
            message = "Patient not found"
            data = {
                'whoami': i_am_hal_read_data_detail,
                'message': message
            }
            print_log('error', i_am_hal_read_data_detail, i_am_hal_read_data_detail, message)
            return Response(data, status=status.HTTP_404_NOT_FOUND)

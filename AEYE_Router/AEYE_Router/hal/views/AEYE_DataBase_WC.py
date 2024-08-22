from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import aeye_database_checkup_models, aeye_database_patient_models
from .serializers import aeye_checkup_serializers

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

i_am_hal_write_data_checkup = 'Router HAL - DataBase Write Checkup'


class aeye_database_checkup_ViewSet(viewsets.ModelViewSet):
    queryset = aeye_database_checkup_models.objects.all()
    serializer_class = aeye_checkup_serializers

    def create(self, request) :
        serializer = aeye_checkup_serializers(data=request.data)        

        patient_name = request.data.get("name")

        print_log('active', i_am_hal_write_data_checkup, i_am_hal_write_data_checkup, request.data)

        try:
            patient = aeye_database_patient_models.objects.get(name=patient_name)
            patient.numberOfVisits += 1
            patient.recentVisitDate = request.data.get("date")

            new_severity = request.data.get("severityPercentage")
            if new_severity and float(new_severity.strip('%')) > float(patient.severityPercentage.strip('%')):
                patient.severityPercentage = new_severity
            
            patient.save()

        except patient.DoesNotExist:
            message="patient Not Found"
            print_log('error', i_am_hal_write_data_checkup, i_am_hal_write_data_checkup, message)
            data={
                'whoami' : i_am_hal_write_data_checkup,
                'message': message
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


        checkup_data = {
            "patientId"        : patient.id,
            "date"             : request.data.get("date"),
            "symptom"          : request.data.get("symptom"),
            "status"           : request.data.get("status"),
            "ultrasound_image" : request.data.get("ultrasound_image"),
            "ai_diagnosis"     : request.data.get("ai_diagnosis"),
            "ai_probability"   : request.data.get("ai_probability"),
            "doctor_diagnosis" : request.data.get("doctor_diagnosis"),
        }

        serializer = aeye_checkup_serializers(data=checkup_data)

        if serializer.is_valid():
            serializer.save() 

            message="Succed to Save at Database Checkup"
            data={
                'whoami' : i_am_hal_write_data_checkup,
                'message': message
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            message="{}".format(serializer.errors)
            print_log('error', i_am_hal_write_data_checkup, i_am_hal_write_data_checkup, message)
            data={
                'whoami' : i_am_hal_write_data_checkup,
                'message': message
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import aeye_database_list_models, aeye_Checkup, aeye_UltrasoundImage, aeye_Report
from .serializers import aeye_database_list_serializers
from colorama import Fore, Back, Style
from datetime import datetime
import requests
import os
from django.db import transaction 


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

i_am_hal_write_data = 'Router HAL - DataBase Write'


class aeye_database_write_list_Viewswets(viewsets.ModelViewSet):
    queryset=aeye_database_list_models.objects.all().order_by('id')
    serializer_class=aeye_database_list_serializers

    def create(self, request) :
        serializer = aeye_database_list_serializers(data = request.data)

        if serializer.is_valid() :
            
            ##############################################
            # MySQL Save List
            try:
                data = serializer.validated_data

                with transaction.atomic():  # 트랜잭션 시작
                    # Patient 정보 저장
                    patient = aeye_database_list_models.objects.create(
                        id=data['id'],
                        name=data['name'],
                        DOB=data['DOB'],
                        profileImage=data['profileImage'],
                        numberOfVisits=data['numberOfVisits'],
                        recentVisitDate=data['recentVisitDate'],
                        severityPercentage=data['severityPercentage'],
                        status=data['status']
                    )

                    # Checkup 정보 저장
                    for checkup_data in data['checkups']:
                        checkup = aeye_Checkup.objects.create(
                            patient=patient,
                            date=checkup_data['date'],
                            symptom=checkup_data['symptom'],
                            status=checkup_data['status']
                        )

                        # UltrasoundImage 정보 저장
                        for image_url in checkup_data['ultrasoundImages']:
                            aeye_UltrasoundImage.objects.create(
                                checkup=checkup,
                                imageUrl=image_url
                            )

                        # Report 정보 저장
                        report_data = checkup_data['report']
                        aeye_Report.objects.create(
                            checkup=checkup,
                            ai_diagnosis=report_data['ai']['diagnosis'],
                            ai_probability=report_data['ai']['probability'],
                            doctor_diagnosis=report_data['doctor']['diagnosis']
                        )

                message = "Data saved successfully."
                print_log('active', i_am_hal_write_data, i_am_hal_write_data, message)
                data = {
                    'whoami': i_am_hal_write_data,
                    'message': message,
                }
                return Response(data, status=status.HTTP_200_OK)

            except Exception as e:
                message = str(e)
                print_log('error', i_am_hal_write_data, i_am_hal_write_data, message)
                data = {
                    'whoami': i_am_hal_write_data,
                    'message': message
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = serializer.errors
            print_log('error', i_am_hal_write_data, i_am_hal_write_data, "Failed to Receive Data: {}".format(message))

            data = {
                'whoami': i_am_hal_write_data,
                'message': "Failed to Write Data in DataBase"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
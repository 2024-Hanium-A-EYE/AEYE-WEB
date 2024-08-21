from rest_framework import serializers
from .models import (aeye_inference_models, 
                     aeye_database_read_models, 
                     aeye_database_write_models, 
                     aeye_database_list_models,
                     aeye_Checkup_models,
                     aeye_UltrasoundImage_models,
                     aeye_Report_models)

class aeye_inference_serializers(serializers.ModelSerializer):
    
    class Meta:
        model  = aeye_inference_models
        fields = ['whoami', 'image', 'message']


class aeye_database_read_serializers(serializers.ModelSerializer):

    class Meta:
        model  = aeye_database_read_models
        fields = ['whoami', 'message', 'request_data']


class aeye_database_write_serializers(serializers.ModelSerializer):

    class Meta:
        model  = aeye_database_write_models
        fields = ['whoami', 'message', 'request_data']

class aeye_database_list_serializers(serializers.ModelSerializer):
    
    class Meta:
        model  = aeye_database_list_models
        fields = ['id', 'name', 'DOB', 'profileImage', 'numberOfVisits', 'recentVisitDate', 'severityPercentage', 'status', 'checkups']

class aeye_ultrasound_image_Serializers(serializers.ModelSerializer):
    class Meta:
        model = aeye_UltrasoundImage_models
        fields = ['imageUrl']

class aeye_report_serializers(serializers.ModelSerializer):
    class Meta:
        model = aeye_Report_models
        fields = ['ai_diagnosis', 'ai_probability', 'doctor_diagnosis']

class aeye_checkup_serializers(serializers.ModelSerializer):
    ultrasoundImages = aeye_ultrasound_image_Serializers(many=True, read_only=True)
    report = aeye_report_serializers(read_only=True)

    class Meta:
        model = aeye_Checkup_models
        fields = ['id', 'date', 'symptom', 'status', 'ultrasoundImages', 'report']

class aeyeDatabaseListSerializers(serializers.ModelSerializer):
    checkups = aeye_checkup_serializers(many=True, read_only=True)

    class Meta:
        model = aeye_database_list_models
        fields = ['id', 'name', 'DOB', 'profileImage', 'numberOfVisits', 'recentVisitDate', 'severityPercentage', 'status', 'checkups']

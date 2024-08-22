from rest_framework import serializers
from .models import (aeye_inference_models, 
                     aeye_database_read_models, 
                     aeye_database_write_models, 
                     aeye_database_patient_models,
                     aeye_database_checkup_models,
                     )

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

class aeye_checkup_serializers(serializers.ModelSerializer):
    class Meta:
        model = aeye_database_checkup_models
        fields = '__all__'

class aeye_patient_serializer(serializers.ModelSerializer):
    checkups = aeye_checkup_serializers(many=True, read_only=True)

    class Meta:
        model = aeye_database_patient_models
        fields = '__all__'
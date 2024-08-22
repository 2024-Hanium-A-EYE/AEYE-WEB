from rest_framework import serializers
from .models import (aeye_inference_models,  
                     aeye_database_patient_models,
                     aeye_database_checkup_models,
                     aeye_database_read_detail_models,
                     aeye_database_read_list_models
                     )

class aeye_inference_serializers(serializers.ModelSerializer):
    
    class Meta:
        model  = aeye_inference_models
        fields = ['whoami', 'image', 'message']



class aeye_checkup_serializers(serializers.ModelSerializer):
    class Meta:
        model = aeye_database_checkup_models
        fields = '__all__'


class aeye_patient_serializers(serializers.ModelSerializer):
    checkups = aeye_checkup_serializers(many=True, read_only=True)

    class Meta:
        model = aeye_database_patient_models
        fields = '__all__'


class aeye_read_list_serializers(serializers.ModelSerializer):

    class Meta:
        model = aeye_database_read_list_models
        fields = ['whoami', 'message']


class aeye_read_deatil_serializers(serializers.ModelSerializer):

    class Meta:
        model = aeye_database_read_detail_models
        fields = ['whoami', 'message']
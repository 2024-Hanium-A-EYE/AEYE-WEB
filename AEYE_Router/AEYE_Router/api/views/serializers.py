from rest_framework import serializers
from .models import aeye_wno_models, aeye_wlh_models

class aeye_wno_serializers(serializers.ModelSerializer):
    
    image = serializers.ImageField(required=False)

    class Meta:
        model = aeye_wno_models
        fields = ['whoami', 'message', 'image', 'operation']

class aeye_wlh_serializers(serializers.ModelSerializer):
    

    class Meta:
        model = aeye_wlh_models
        fields = ['whoami', 'message']



from rest_framework import serializers
from .models import *


class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = '__all__'


class ResearchWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientific_Research_Work
        fields = '__all__'


class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'

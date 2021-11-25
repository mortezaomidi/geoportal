from django.db.models import fields
from rest_framework import serializers

from .models import Organization


class OrganizationModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organization
        fields = '__all__'
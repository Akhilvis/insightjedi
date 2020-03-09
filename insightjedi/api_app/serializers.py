from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    # document_owner = serializers.PrimaryKeyRelatedField(source='owner', queryset=User.objects.all())

    class Meta:
        model = Document
        fields = '__all__'

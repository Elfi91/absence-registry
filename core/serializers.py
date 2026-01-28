from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework import serializers
from .models import Absence

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = ['id', 'student', 'date', 'is_justified', 'comment', 'created_by']
        read_only_fields = ['created_by'] # Il creatore viene impostato automaticamente dalla vista
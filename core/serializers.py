from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Absence
from students.serializers import StudentSerializer

# Questo mancava nel file che abbiamo aggiornato prima!
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
    student_details = StudentSerializer(source='student', read_only=True)

    class Meta:
        model = Absence
        fields = ['id', 'student', 'student_details', 'date', 'is_justified', 'comment', 'created_by']
        read_only_fields = ['created_by']
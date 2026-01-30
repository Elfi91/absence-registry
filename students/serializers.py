from rest_framework import serializers
from .models import Student
from core.models import Absence

class StudentAbsenceSerializer(serializers.ModelSerializer):
    """Serializer leggero per mostrare le assenze dentro lo studente"""
    class Meta:
        model = Absence
        fields = ['id', 'date', 'is_justified']

class StudentSerializer(serializers.ModelSerializer):
    absence_percentage = serializers.SerializerMethodField()
    absences = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'course', 'absence_percentage', 'absences']

    def get_absence_percentage(self, obj):
        total_lessons = 100  # Puoi cambiare questo numero in base al corso
        absences_count = obj.absences.count()  # Conta le assenze collegate

        if total_lessons > 0:
            percentage = (absences_count / total_lessons) * 100
            return f"{percentage}%"
        return "0%"
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from students.models import Student
from students.serializers import StudentSerializer

from .models import Absence
from .serializers import AbsenceSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class AbsenceCreateView(generics.ListCreateAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Questo salva l'utente che sta usando Postman come "creatore" dell'assenza
        serializer.save(created_by=self.request.user)
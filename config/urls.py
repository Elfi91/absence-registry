from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import RegisterView, StudentListView, AbsenceCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication Endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Students Endpoints
    path('api/students/', StudentListView.as_view(), name='student_list'),

    # Absences
    path('api/absences/', AbsenceCreateView.as_view(), name='absence_create'),
]
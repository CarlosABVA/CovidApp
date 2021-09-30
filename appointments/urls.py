from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-appointment/', views.AppointmentCreation.as_view(), name='create-appointment'),
    path('appointments/', views.AppointmentList.as_view(), name='appointments-list'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

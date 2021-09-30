from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Appointment
from .serializers import AppointmentSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    View for API root.
    Doesn't need autentication.
    Provides URL's to 'AppointmentCreation' and 'AppointmentList' views.
    """
    return Response({
        'appointment creation': reverse('create-appointment', request=request, format=format),
        'appointment list': reverse('appointments-list', request=request, format=format)
    })

class AppointmentCreation(generics.CreateAPIView):
    """
    View to create an appointment.
    Doesn't need autentication.
    Only allows POST action.
    """
    serializer_class = AppointmentSerializer


class AppointmentList(generics.ListAPIView):
    """
    View to see all appointments.
    Needs autentication.
    Only allows get action.
    Search option by "cip_code" available.
    """
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Appointment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['cip_code']


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to see a particular appointment's details.
    Needs autentication.
    Allows GET, PUT, PATCH and DELETE actions.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    #the serializer gets all fiels from model
    class Meta:
        model = Appointment
        fields = '__all__'

    #override 'to_representation' method to show center_name's name instead of id number
    def to_representation(self, instance):
        rep = super(AppointmentSerializer, self).to_representation(instance)
        rep['center_name'] = instance.center_name.center_name
        return rep
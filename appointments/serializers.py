from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Appointment

from django.utils import timezone
import datetime
import re


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
    
    #validate methods to apply field restrictions
    def validate_cip_code(self, value):
        rule = re.compile(r'^[A-Z]{4}[0-9]{10}\b')
        if not rule.search(value):
            raise ValidationError(r"Invalid CIP code. Must be of format 'AAAA0000000000'.")
        return value
    
    def validate_dni_code(self, value):
        rule = re.compile(r'^[0-9]{8}[A-Z]{1}\b')
        if not rule.search(value):
            raise ValidationError(r"Invalid DNI code. Must be of format '00000000A'.")
        return value    
    
    def validate_app_date(self, value):
        valid_time = timezone.now() + datetime.timedelta(days=1)
        if value < valid_time:
            raise ValidationError("Invalid Appointment date. Must be at least 24h in advance.")

        if value.hour < 8 or value.hour > 21:
            raise ValidationError("Invalid Appointment date. Available hours are from 8:00 to 21:00")
    
        return value
    
    def validate(self, data):
        #ensure there aren't two appointments at the same time in a center
        #must be a 10 minute lapse between appointments
        already_taken = Appointment.objects.filter(
            center_name=data['center_name'], 
            app_date__range=(
                data['app_date'] - datetime.timedelta(minutes=10),
                data['app_date'] + datetime.timedelta(minutes=10)
            )
        )
        if already_taken:
            raise ValidationError("Requested time is already taken.")
            
        return data
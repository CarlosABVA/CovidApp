from django.contrib import admin

from .models import Center, Appointment

admin.site.register(Appointment)
admin.site.register(Center)
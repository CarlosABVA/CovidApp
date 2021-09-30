from django.db import models

class Center(models.Model):
    center_name = models.CharField(max_length=200)
    center_address = models.CharField(max_length=200, default='')
    
    class Meta:
        ordering = ['center_name']

    def __str__(self):
        return self.center_name

class Appointment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni_code =  models.CharField(max_length=9)
    cip_code = models.CharField(max_length=14)
    birth_date = models.DateField()
    app_date = models.DateTimeField('Appointment date', auto_now=False)
    center_name = models.ForeignKey(Center, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return '{0} '.format(self.cip_code) + '{:%Y-%m-%d %H:%M:%S}'.format(self.created_date)
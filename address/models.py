from django.db import models

# Create your models here.
class Address(models.Model):
    city=models.CharField("adr_city",max_length=50)
    pincode = models.IntegerField("adr_pin")
    state = models.CharField("adr_state", max_length=50)
    active = models.CharField("active", max_length=50, default='Y')

    class Meta:
        db_table ='Address_Info'
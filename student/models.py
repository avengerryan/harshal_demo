from django.db import models

# Create your models here.
from address.models import Address

class Student(models.Model):
    studname=models.CharField("stud_name",max_length=50)
    studage = models.IntegerField("stud_age")
    studemail = models.EmailField("stud_email", max_length=50)
    studfees = models.FloatField("stud_fees")
    studdept = models.CharField("stud_dept", max_length=50)
    active = models.CharField("active", max_length=50,default='Y')
    studAddress = models.OneToOneField(Address,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table ='Stud_Info'
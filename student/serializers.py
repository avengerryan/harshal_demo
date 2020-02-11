from rest_framework.serializers import ModelSerializer
from student.models import Student
from address.serializers import CustomeAddressSerializer,AddressSerializer
class StudentSerializer(ModelSerializer):
    studAddress = AddressSerializer
    class Meta:
        model = Student
        exclude=('active',)
        #fields = '__all__'
        #fields=('id','studname','studage')
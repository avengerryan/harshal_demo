from rest_framework.serializers import ModelSerializer
from address.models import Address



class CustomeAddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields=("city",)

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude=('active',)
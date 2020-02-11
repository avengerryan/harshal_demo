from rest_framework.routers import  SimpleRouter
from address.views import AddressOpearations
routing = SimpleRouter()
routing.register('address',AddressOpearations)

urlpatterns = routing.urls

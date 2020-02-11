from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='EndPoints for College App')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^swagger/', schema_view),
    url('api/v1/',include('address.router')),
    url('api/v1/',include('student.router'))
]

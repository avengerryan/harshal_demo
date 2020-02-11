from rest_framework.routers import SimpleRouter
from student.views import StudentOpearations
routing = SimpleRouter()
routing.register('student',StudentOpearations)
urlpatterns = routing.urls

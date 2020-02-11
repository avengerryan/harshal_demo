
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet

class StudentOpearations(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
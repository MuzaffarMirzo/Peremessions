


from rest_framework import permissions
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Courses,Teachers,Students
from .serializers import CourseSerializer, TeacherSerializer, StudentSerializer



class CourseListCreateView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class TeacherListCreateView(ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class TeacherRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class StudentListCreateView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
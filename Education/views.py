from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny

from .models import Courses, Teachers, Students
from .serializers import CourseSerializer, TeacherSerializer, StudentSerializer




class CourseAPICreate(generics.ListCreateAPIView):
    
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class CourseAPIUpdDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class TeacherAPICreate(generics.ListCreateAPIView):
    
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class TeacherAPIUpdDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class StudentAPICreate(generics.ListCreateAPIView):
    
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class StudentAPIUpdDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




def index(request):
    return render(request, 'index.html')
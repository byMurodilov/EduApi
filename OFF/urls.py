"""
URL configuration for OFF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Education.views import CourseAPICreate, CourseAPIUpdDestroy, TeacherAPICreate, TeacherAPIUpdDestroy, StudentAPICreate, StudentAPIUpdDestroy, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/v1/courses/', CourseAPICreate.as_view(), name='course-list-create'),
    path('api/v1/courses/<int:pk>/', CourseAPIUpdDestroy.as_view(), name='course-detail'),
    path('api/v1/teachers/', TeacherAPICreate.as_view(), name='teacher-list-create'),
    path('api/v1/teachers/<int:pk>/', TeacherAPIUpdDestroy.as_view(), name='teacher-detail'),
    path('api/v1/students/', StudentAPICreate.as_view(), name='student-list-create'),
    path('api/v1/students/<int:pk>/', StudentAPIUpdDestroy.as_view(), name='student-detail'),
]

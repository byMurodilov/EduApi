from django.contrib import admin
from .models import Courses, Teachers, Students


admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(Students)
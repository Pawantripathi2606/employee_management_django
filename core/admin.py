from django.contrib import admin
from .models import Employee, Notice, Attendance, Work, Request

admin.site.register(Employee)
admin.site.register(Notice)
admin.site.register(Attendance)
admin.site.register(Work)
admin.site.register(Request)

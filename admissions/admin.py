from django.contrib import admin
from admissions.models import student
from admissions.models import Teacher


class studentadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'fathername', 'classname', 'contact']


class teacheradmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'exp', 'subject', 'contact']


# Register your models here.
admin.site.register(student, studentadmin)
admin.site.register(Teacher, teacheradmin)

from django.urls import path
from admissions.views import addadmin
from admissions.views import adminreport
from admissions.views import addvendor
from admissions.views import deletestudent
from admissions.views import updatestudent
from admissions.views import FirstClassView
from admissions.views import TeacherRead
from admissions.views import getTeacher
from admissions.views import AddTeacher
from admissions.views import UpdateTeacher
from admissions.views import RemoveTeacher
urlpatterns = [
    path('newadmin/', addadmin),
    path('adminreport/', adminreport),
    path('newvendor/', addvendor),
    path('delete/<int:id>', deletestudent),
    path('update/<int:id>', updatestudent),
    path('firstcbv/', FirstClassView.as_view()),
    path('teacherlist/',TeacherRead.as_view(),name='listteachers'),
    path('getteacher/<int:pk>/',getTeacher.as_view()),
    path('insertteacher/',AddTeacher.as_view()),
    path('updateteacher/<int:pk>/',UpdateTeacher.as_view()),
    path('removeteacher/<int:pk>/',RemoveTeacher.as_view()),
]
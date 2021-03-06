"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from Syllabus_Project.views import Login, Admin, AddCourse, AddUser, userView, TAView, \
    AddPersonalInfo, AddSection, Policy, DeleteUsers, DeleteCourses, DeleteSections, Syllabus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name="login"),
    path('adminPage', Admin.as_view(), name="adminPage"),
    path('addUser', AddUser.as_view(), name="adduser"),
    path('addCourse', AddCourse.as_view(), name="addcourse"),
    path('addSection', AddSection.as_view(), name="addSection"),
    path('userView', userView.as_view(), name="userView"),
    path('TAView', TAView.as_view(), name="TAView"),
    path('AddPersonalInfo', AddPersonalInfo.as_view(), name="AddPersonalInfo"),
    path('addPolicy', Policy.as_view(), name='AddPolicy'),
    path('deleteUser', DeleteUsers.as_view(), name='deleteUser'),
    path('deleteCourse', DeleteCourses.as_view(), name='deleteCourse'),
    path('deleteSection', DeleteSections.as_view(), name='deleteSection'),
    re_path(r'^syllabus/(?P<year>[0-9]{4})/(?P<semester>[a-zA-Z]+)/(?P<courseNumber>[0-9]{3})', Syllabus.as_view(), name="syllabus")
]

"""
URL configuration for luiza project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from user.api.viewsets import UserViewset, StudentViewset
from report_card_grades.api.viewsets import ReportCardViewset
from scheduler.api.viewsets import SchedulerViewset
from classes.api.viewsets import (
    VideoViewset,
    ClassViewset
)
from school_year.api.viewsets import SchoolYearViewset
from live.urls import urlpatterns as livestream_urls
from rules.api.viewsets import RuleViewset
from school_subject.api.viewsets import SubjectViewset
from administrative.api.viewsets import AdministrativeViewset
from notifications.api.viewsets import NotificationViewset


router = routers.DefaultRouter()
router.register(
    r'users', 
    UserViewset, 
    basename='User'
)
router.register(
    r'reports_card', 
    ReportCardViewset, 
    basename='ReportCard'
)
router.register(
    r'scheduler', 
    SchedulerViewset, 
    basename='Scheduler'
)
router.register(
    r'school_year', 
    SchoolYearViewset, 
    basename='SchoolYear'
)
router.register(
    r'video', 
    VideoViewset, 
    basename='Video'
)
router.register(
    r'rule', 
    RuleViewset, 
    basename='Rules'
)
router.register(
    r'subject', 
    SubjectViewset, 
    basename='Subject'
)
router.register(
    r'administrative', 
    AdministrativeViewset, 
    basename='Administrative'
)
router.register(
    r'class', 
    ClassViewset, 
    basename='Class'
)
router.register(
    r'student', 
    StudentViewset, 
    basename='Student'
)
router.register(
    r'notification', 
    NotificationViewset, 
    basename='Notification'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('livestream/', include('live.urls')),
    path('auth/login/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

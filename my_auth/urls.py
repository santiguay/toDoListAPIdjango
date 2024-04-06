from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
 
    re_path('login/',views.login),
    re_path('register/',views.register),
    re_path('profile/',views.profile),
    path('api/v0/', include(router.urls)),
    
]
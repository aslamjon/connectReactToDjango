from django.contrib import admin
from django.urls import path, include
from .views import index, StudentViewset
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'student', StudentViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', obtain_auth_token),
]

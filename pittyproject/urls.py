from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pittyapi.views import *


router = routers.DefaultRouter(trailing_slash=False)

router.register(r"users", Users, "user")
router.register(r"adopters", AdoptersViewSet, "adopter")


urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
]

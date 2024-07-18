from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pittyapi.views import register_user, login_user, Users


router = routers.DefaultRouter(trailing_slash=False)

router.register(r"users", Users, "user")


urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
]

from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.conf import settings

from rest_framework import routers
from pittyapi.views import *


router = routers.DefaultRouter(trailing_slash=False)

router.register(r"users", Users, "user")
router.register(r"adopters", AdoptersViewSet, "adopter")
router.register(r"dogs", DogViewSet)
router.register(r"adoptions", AdoptionViewSet)
router.register(r"applications", ApplicationViewSet)
router.register(r"events", EventViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    
]

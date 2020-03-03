from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('document/', Document.as_view(), name="Document-api")

]

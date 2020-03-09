from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('document/', DocumentList.as_view()),
    path('document/<int:pk>/', DocumentDetail.as_view()),
    path('document/delete/<int:pk>/', DocumentDetail.as_view()),
]

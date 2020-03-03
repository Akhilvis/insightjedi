from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import DocumentSerializer


# Create your views here.


class Document(APIView):
    """Get, create and delete apis"""

    def get(self, request):
        print('222222222222222222222222222')
from django.shortcuts import render
from .models import Personal
from .serializer import PersonalSerializer
from rest_framework import viewsets

# Create your views here.

class PersonalViewset(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
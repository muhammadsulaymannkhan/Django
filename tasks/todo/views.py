from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Todo
from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    filter_backends=(filters.DjangoFilterBackend,)
    
    filterset_fields=('name','id')

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['name', 'content']
    # name = serializers.CharField(max_length=255)
    # content = serializers.CharField(max_length=1000)
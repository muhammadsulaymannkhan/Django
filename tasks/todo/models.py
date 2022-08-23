from ast import Attribute
from django.db import models

class Todo(models.Model):
    class Meta:
        db_table="todo"
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


from django.contrib import admin
from .models import Todo

class TodoAdminModel(admin.ModelAdmin):
    search_fields=('name',)
# Register your models here.
admin.site.register(Todo,TodoAdminModel)

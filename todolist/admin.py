from django.contrib import admin

from .models import ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'date', 'user', 'check']
    list_display_links = ['id', 'task']

admin.site.register(ToDoList, ToDoListAdmin)
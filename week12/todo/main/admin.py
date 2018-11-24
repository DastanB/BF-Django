from django.contrib import admin
from .models import Task, List

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('title', 'name')
    list_per_page = 25

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'due_on', 'user', 'mark', 'list')
    list_display_links = ('id', 'name', 'created', 'due_on', 'user', 'mark', 'list')
    search_fields = ('title', 'name', 'created', 'due_on', 'user', 'mark', 'list')
    list_per_page = 25


admin.site.register(Task, TaskAdmin)
admin.site.register(List, ListAdmin)
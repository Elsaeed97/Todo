from django.contrib import admin
from .models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ('title','completed','created')



admin.site.register(Task, TaskAdmin)
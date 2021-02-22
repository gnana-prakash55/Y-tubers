from django.contrib import admin
from .models import Hiretubers


class HtAdmin(admin.ModelAdmin):
    list_display = ('firstname','email','tuber_name')

admin.site.register(Hiretubers,HtAdmin)
from django.contrib import admin
from .models import Contactinfo


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','phone')

admin.site.register(Contactinfo,ContactAdmin)


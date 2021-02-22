from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,obj):
        return format_html('<img src="{}" width="40"/>'.format(obj.photo.url))

    list_display = ('id','myphoto','first_name','role','created_date')
    list_display_links = ('first_name',)
    search_fields = ('id','role')


class SliderAdmin(admin.ModelAdmin):

    def myphoto(self,obj):
        return format_html('<img src="{}" width="60" height="40"/>'.format(obj.photo.url))
    
    list_display = ('headline','myphoto','button_text')



admin.site.register(Slider,SliderAdmin)
admin.site.register(Team,TeamAdmin) 
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Youtuber(models.Model):
    crew_choices = (
        ('Solo','Solo'),
        ('Small','Small'),
        ('Large','Large'),
    )
    camera_choices = (
        ('Nikon','Nikon'),
        ('Canon','Canon'),
        ('Sony','Sony'),
        ('Other','Other'),
    )
    category_choices = (
        ('Coding','Coding'),
        ('Tech review','Tech review'),
        ('Vlogs','Vlogs'),
        ('Comedy','Comedy'),
        ('Gaming','Gaming'),
        ('Cooking','Cooking'),
        ('Other','Other'),
    )

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=100)
    description = RichTextField()
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=50)
    camera_type = models.CharField(choices=camera_choices,max_length=50)
    subs_count = models.CharField(max_length=50)
    category = models.CharField(choices=category_choices,max_length=50)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
  
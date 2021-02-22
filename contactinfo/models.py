from django.db import models

class Contactinfo(models.Model):
    email = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    fb_link = models.CharField(max_length=50)
    insta_link = models.CharField(max_length=50)
    twitter_link = models.CharField(max_length=50)
    yt_link = models.CharField(max_length=50)
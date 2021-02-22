from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=25)
    fb_link = models.CharField(max_length=100)
    insta_link = models.CharField(max_length=100)
    yt_link = models.CharField(max_length=50,default='https://www.youtube.com')
    created_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    url = models.CharField(max_length=25,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
    

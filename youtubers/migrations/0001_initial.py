# Generated by Django 3.0.5 on 2020-12-29 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%Y/%m/')),
                ('video_url', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(max_length=50)),
                ('camera_type', models.CharField(max_length=50)),
                ('subs_count', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]

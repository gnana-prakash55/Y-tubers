# Generated by Django 3.0.5 on 2021-01-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('fb_link', models.CharField(max_length=50)),
                ('insta_link', models.CharField(max_length=50)),
                ('twitter_link', models.CharField(max_length=50)),
                ('yt_link', models.CharField(max_length=50)),
            ],
        ),
    ]

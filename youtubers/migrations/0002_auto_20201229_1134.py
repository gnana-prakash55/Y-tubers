# Generated by Django 3.0.5 on 2020-12-29 11:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('nikon', 'Nikon'), ('canon', 'Canon'), ('sony', 'Sony'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('coding', 'Coding'), ('tech_review', 'Tech review'), ('vlogs', 'Vlogs'), ('comedy', 'Comedy'), ('gaming', 'Gaming'), ('cooking', 'Cooking'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'Solo'), ('small', 'Small'), ('large', 'Large')], max_length=50),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

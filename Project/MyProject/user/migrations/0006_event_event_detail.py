# Generated by Django 3.2.4 on 2023-09-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_imagegallery_videogallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_detail',
            field=models.TextField(null=True),
        ),
    ]

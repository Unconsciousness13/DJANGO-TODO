# Generated by Django 4.1.3 on 2022-11-24 11:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_usersgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersgroup',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
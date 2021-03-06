# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-04-25 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ping_title', models.CharField(max_length=512)),
                ('ping_message', models.CharField(max_length=512)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ping', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IMAGES',
            new_name='IMAGE',
        ),
        migrations.RenameModel(
            old_name='TAGS',
            new_name='TAG',
        ),
    ]
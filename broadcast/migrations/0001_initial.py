# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=20)),
                ('video', models.FileField(upload_to=b'video/', blank=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 5, 27, 8, 45, 8, 975691, tzinfo=utc))),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('verbose_title', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(upload_to=b'scc/images/', blank=True)),
                ('private', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0003_auto_20150527_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('skype', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to=b'images/consultants/')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 3, 15, 40, 23, 691202, tzinfo=utc)),
        ),
    ]

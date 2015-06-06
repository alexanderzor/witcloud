# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0004_auto_20150603_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='phone_number',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='skype',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 4, 14, 29, 20, 450390, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0002_auto_20150527_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 5, 27, 8, 47, 58, 241550, tzinfo=utc)),
        ),
    ]

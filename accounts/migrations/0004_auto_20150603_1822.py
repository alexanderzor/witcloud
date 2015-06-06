# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150516_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='my_needs', to='accounts.CustomUser', null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Thank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='my_thanks', to='accounts.CustomUser', null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('need_id', models.ForeignKey(to='accounts.Need')),
                ('user_id', models.ForeignKey(to='accounts.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='need',
            name='voters',
            field=models.ManyToManyField(to='accounts.CustomUser', through='accounts.Votes'),
        ),
    ]

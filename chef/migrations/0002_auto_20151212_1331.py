# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='user',
        ),
        migrations.AddField(
            model_name='chef',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 12, 12, 13, 30, 51, 797008, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chef',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 12, 12, 13, 31, 15, 807311, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chef',
            name='password',
            field=models.CharField(default=datetime.datetime(2015, 12, 12, 13, 31, 24, 64082, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]

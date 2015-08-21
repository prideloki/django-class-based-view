# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150821_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 21, 10, 49, 52, 437271, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

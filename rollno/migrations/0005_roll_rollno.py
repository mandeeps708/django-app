# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollno', '0004_auto_20150106_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='rollno',
            field=models.PositiveSmallIntegerField(default=125045),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollno', '0003_auto_20150106_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roll',
            name='age',
            field=models.PositiveSmallIntegerField(default=10),
            preserve_default=True,
        ),
    ]

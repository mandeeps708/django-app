# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='age',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
            preserve_default=False,
        ),
    ]

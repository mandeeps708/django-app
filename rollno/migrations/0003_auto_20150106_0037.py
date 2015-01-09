# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollno', '0002_roll_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='email',
            field=models.EmailField(default=b'abc@xyz.com', max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roll',
            name='age',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]

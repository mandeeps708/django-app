# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollno', '0005_roll_rollno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roll',
            old_name='rollno',
            new_name='collegerollno',
        ),
    ]

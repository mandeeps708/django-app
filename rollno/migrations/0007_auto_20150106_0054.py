# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollno', '0006_auto_20150106_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roll',
            old_name='collegerollno',
            new_name='college_Rollno',
        ),
    ]

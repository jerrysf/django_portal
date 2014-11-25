# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_product_phases_majorregression'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_phases',
            name='majorRegression',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

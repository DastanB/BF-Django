# Generated by Django 2.0.5 on 2018-11-10 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181110_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 10, 13, 59, 52, 681636)),
        ),
    ]

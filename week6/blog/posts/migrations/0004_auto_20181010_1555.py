# Generated by Django 2.0.5 on 2018-10-10 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181005_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 15, 54, 59, 208388)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 15, 54, 59, 207388), null=True),
        ),
    ]

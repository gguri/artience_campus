# Generated by Django 2.0.4 on 2018-08-03 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20180801_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 3, 9, 58, 19, 250989)),
        ),
    ]

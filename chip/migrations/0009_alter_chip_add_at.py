# Generated by Django 4.1 on 2022-09-04 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chip', '0008_alter_chip_add_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='add_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
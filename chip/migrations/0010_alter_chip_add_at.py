# Generated by Django 4.1 on 2022-09-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chip', '0009_alter_chip_add_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='add_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.1 on 2022-08-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chiptoconvert', '0007_alter_chiptoconvert_serial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiptoconvert',
            name='serial',
            field=models.CharField(blank=True, default='--', max_length=50),
        ),
        migrations.AlterField(
            model_name='chiptoconvert',
            name='x',
            field=models.CharField(blank=True, default='--', max_length=200),
        ),
    ]

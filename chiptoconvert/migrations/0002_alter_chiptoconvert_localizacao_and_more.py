# Generated by Django 4.1 on 2022-08-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chiptoconvert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiptoconvert',
            name='localizacao',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='chiptoconvert',
            name='operadora',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='chiptoconvert',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]

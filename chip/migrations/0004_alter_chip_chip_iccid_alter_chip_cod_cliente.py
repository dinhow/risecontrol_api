# Generated by Django 4.1 on 2022-08-31 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chip', '0003_alter_chip_chip_iccid_alter_chip_chip_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='chip_iccid',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='chip',
            name='cod_cliente',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
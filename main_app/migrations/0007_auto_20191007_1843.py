# Generated by Django 2.2.5 on 2019-10-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20191007_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_calendarioservicio',
            name='domicilio',
            field=models.CharField(default='', max_length=100),
        ),
    ]

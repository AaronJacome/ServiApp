# Generated by Django 2.2.5 on 2019-10-09 16:33

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20191007_1815'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='tb_calendarioservicio',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tb_catalogoservicio',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tb_usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
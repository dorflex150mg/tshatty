# Generated by Django 2.0.7 on 2021-01-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_auto_20210123_1303'),
    ]

    operations = [
        migrations.DeleteModel(
            name='friend',
        ),
    ]
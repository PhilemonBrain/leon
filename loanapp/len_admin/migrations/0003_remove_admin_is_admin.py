# Generated by Django 3.0.7 on 2020-08-19 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('len_admin', '0002_auto_20200819_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='is_admin',
        ),
    ]
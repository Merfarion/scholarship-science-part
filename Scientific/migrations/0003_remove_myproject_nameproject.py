# Generated by Django 3.1.7 on 2021-03-31 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scientific', '0002_auto_20210331_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myproject',
            name='nameproject',
        ),
    ]
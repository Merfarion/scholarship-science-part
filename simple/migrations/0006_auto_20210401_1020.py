# Generated by Django 3.1.7 on 2021-04-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0005_remove_myproject_nameproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='place',
            field=models.IntegerField(default=5, verbose_name='Занятое место'),
        ),
    ]

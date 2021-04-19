# Generated by Django 3.1.7 on 2021-04-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scientific', '0008_auto_20210412_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmation_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('admin', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyProject',
        ),
        migrations.AddField(
            model_name='grant',
            name='scores',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='patent',
            name='scores',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='publications',
            name='scores',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='scientific_research_work',
            name='scores',
            field=models.IntegerField(default=-1),
        ),
    ]
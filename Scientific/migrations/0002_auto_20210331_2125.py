# Generated by Django 3.1.7 on 2021-03-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scientific', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameproject', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='MySimpleModel',
        ),
    ]
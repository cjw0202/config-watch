# Generated by Django 2.1.8 on 2020-04-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200409_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configfile',
            name='update_time',
            field=models.DateField(),
        ),
    ]

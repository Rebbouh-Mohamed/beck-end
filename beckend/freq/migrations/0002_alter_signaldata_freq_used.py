# Generated by Django 5.2 on 2025-04-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signaldata',
            name='freq_used',
            field=models.IntegerField(default=0),
        ),
    ]

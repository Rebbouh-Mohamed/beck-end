# Generated by Django 5.2 on 2025-04-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('users', models.IntegerField()),
                ('signal', models.FloatField()),
                ('freq_used', models.IntegerField()),
            ],
        ),
    ]

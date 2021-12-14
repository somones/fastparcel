# Generated by Django 3.1.3 on 2021-01-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210109_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
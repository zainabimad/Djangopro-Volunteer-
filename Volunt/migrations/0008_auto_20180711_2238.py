# Generated by Django 2.0.6 on 2018-07-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunt', '0007_auto_20180711_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='study',
            name='certificate',
            field=models.CharField(max_length=50),
        ),
    ]

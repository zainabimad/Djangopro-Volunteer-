# Generated by Django 2.0.6 on 2018-08-03 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Images', '0003_auto_20180803_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded',
            name='img',
            field=models.FileField(upload_to='docs/'),
        ),
    ]

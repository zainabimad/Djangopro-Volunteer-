# Generated by Django 2.0.6 on 2018-08-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploaded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('info', models.CharField(blank=True, max_length=400)),
                ('img', models.ImageField(height_field=500, max_length=600, upload_to='media/', width_field=500)),
                ('up_date', models.DateField(auto_now_add=True)),
                ('uploader', models.CharField(max_length=200)),
            ],
        ),
    ]

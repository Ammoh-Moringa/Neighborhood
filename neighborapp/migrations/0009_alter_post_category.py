# Generated by Django 3.2.5 on 2021-07-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0008_auto_20210725_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=120),
        ),
    ]

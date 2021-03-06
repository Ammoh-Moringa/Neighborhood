# Generated by Django 3.2.5 on 2021-07-25 12:12

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighborapp', '0007_neighbourhood_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='neighbourhood_location',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='neighbourhood_name',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='occupants_count',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nieghborhood_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_location',
            field=models.CharField(default=datetime.datetime(2021, 7, 25, 12, 12, 18, 755550, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_name',
            field=models.CharField(default=datetime.datetime(2021, 7, 25, 12, 12, 43, 406072, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_photo',
            field=cloudinary.models.CloudinaryField(default='photo', max_length=255, verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='idNo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborapp.neighbourhood'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Crimes and Safety'), ('2', 'Health Emergency'), ('3', 'Recommendations'), ('4', 'Fire Breakouts'), ('5', 'Lost and Found'), ('6', 'Death'), ('7', 'Event')], max_length=120)),
                ('title', models.CharField(max_length=100, null=True)),
                ('post', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_post', to='neighborapp.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='neighborapp.profile')),
            ],
        ),
    ]

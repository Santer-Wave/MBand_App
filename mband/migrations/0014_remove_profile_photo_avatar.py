# Generated by Django 4.0.3 on 2022-04-06 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mband.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mband', '0013_alter_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=mband.models.upload_to, verbose_name='Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-31 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mband', '0004_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkvk',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
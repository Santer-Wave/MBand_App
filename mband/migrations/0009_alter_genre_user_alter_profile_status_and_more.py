# Generated by Django 4.0.3 on 2022-04-06 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mband', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Нет статуса'), (2, 'В поисках группы'), (3, 'В поисках людей в группу')], default=(1, 'Нет статуса'), max_length=64),
        ),
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
    ]

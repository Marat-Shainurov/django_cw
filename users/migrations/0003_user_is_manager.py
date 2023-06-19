# Generated by Django 4.2.1 on 2023-06-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_verified_user_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='is_user_manager'),
        ),
    ]

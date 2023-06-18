# Generated by Django 4.2.1 on 2023-06-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='is_email_verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, null=True, verbose_name='email_verification_code'),
        ),
    ]

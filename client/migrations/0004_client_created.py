# Generated by Django 4.2.1 on 2023-06-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='is_manager'),
        ),
    ]

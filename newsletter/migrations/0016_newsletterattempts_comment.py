# Generated by Django 4.2.1 on 2023-06-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0015_remove_newsletterattempts_email_server_response_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterattempts',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Error message or comment'),
        ),
    ]

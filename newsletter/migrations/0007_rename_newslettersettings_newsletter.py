# Generated by Django 4.2.1 on 2023-06-05 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_alter_newslettersettings_content_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSettings',
            new_name='Newsletter',
        ),
    ]

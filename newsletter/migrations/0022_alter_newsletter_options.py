# Generated by Django 4.2.1 on 2023-06-27 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0021_alter_newsletterattempts_attempt_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('remove_regular_newsletter', 'can remove regular newsletter')], 'verbose_name': 'Newsletter', 'verbose_name_plural': 'Newsletters'},
        ),
    ]

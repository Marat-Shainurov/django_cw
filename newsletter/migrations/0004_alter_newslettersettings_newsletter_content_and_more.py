# Generated by Django 4.2.1 on 2023-06-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_newslettersettings_newsletter_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersettings',
            name='newsletter_content',
            field=models.TextField(verbose_name='newsletter_content'),
        ),
        migrations.AlterField(
            model_name='newslettersettings',
            name='newsletter_subject',
            field=models.CharField(max_length=100, verbose_name='newsletter_subject'),
        ),
    ]

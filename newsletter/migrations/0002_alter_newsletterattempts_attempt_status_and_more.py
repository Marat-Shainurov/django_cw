# Generated by Django 4.2.1 on 2023-06-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletterattempts',
            name='attempt_status',
            field=models.CharField(blank=True, choices=[('success', 'Success'), ('failure', 'Failure'), ('in_progress', 'In_progress')], max_length=12, null=True, verbose_name='attempt_status'),
        ),
        migrations.AlterField(
            model_name='newslettersettings',
            name='regularity',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=10, verbose_name='newsletter_regularity'),
        ),
    ]

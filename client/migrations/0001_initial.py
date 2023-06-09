# Generated by Django 4.2.1 on 2023-06-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='client_name')),
                ('email', models.EmailField(max_length=50, verbose_name='client_email')),
                ('is_signed_up', models.BooleanField(default=True)),
                ('comments', models.TextField(verbose_name='additional_info')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
    ]

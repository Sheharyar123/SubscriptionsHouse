# Generated by Django 4.1.5 on 2023-03-08 13:51

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]

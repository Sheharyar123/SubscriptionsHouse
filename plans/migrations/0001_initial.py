# Generated by Django 4.1.5 on 2023-03-07 13:34

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('background_type', models.CharField(choices=[('primary', 'primary'), ('secondry', 'secondry'), ('danger', 'danger')], max_length=30)),
                ('plan_type', models.CharField(blank=True, choices=[('BASIC', 'BASIC'), ('POPULAR', 'POPULAR'), ('ENTERPRISE', 'ENTERPRISE')], max_length=30, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('title', models.CharField(max_length=255)),
                ('valid_for', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('active', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_on', 'added_on'],
            },
        ),
    ]

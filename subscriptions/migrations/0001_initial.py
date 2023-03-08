# Generated by Django 4.1.5 on 2023-03-08 13:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('valid_from', models.DateTimeField(blank=True, null=True)),
                ('valid_till', models.DateTimeField(blank=True, null=True)),
                ('subscribed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='plans.plan')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]

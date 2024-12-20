# Generated by Django 5.1.2 on 2024-12-02 04:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_userprofile_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('promotion_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsvp_status', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='events.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
    ]

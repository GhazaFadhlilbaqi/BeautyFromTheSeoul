# Generated by Django 5.1.2 on 2024-10-23 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_userprofile_email_remove_userprofile_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

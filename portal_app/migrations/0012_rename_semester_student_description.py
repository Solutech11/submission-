# Generated by Django 3.2.5 on 2021-11-18 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_app', '0011_auto_20211117_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='semester',
            new_name='Description',
        ),
    ]

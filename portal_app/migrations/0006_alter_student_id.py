# Generated by Django 3.2.5 on 2021-11-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_app', '0005_auto_20211115_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-11-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_app', '0008_alter_student_image_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='File_Attachment',
            field=models.FileField(blank=True, null=True, upload_to='media/%d/%m/%y'),
        ),
    ]

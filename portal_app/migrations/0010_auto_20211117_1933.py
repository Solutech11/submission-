# Generated by Django 3.2.5 on 2021-11-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_app', '0009_alter_student_file_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='File_Attachment',
            field=models.FileField(blank=True, null=True, upload_to='%d/%m/%y'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Image_Attachment',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

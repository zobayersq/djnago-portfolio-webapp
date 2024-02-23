# Generated by Django 5.0.2 on 2024-02-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
    ]

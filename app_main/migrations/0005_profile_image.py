# Generated by Django 4.1 on 2023-07-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]

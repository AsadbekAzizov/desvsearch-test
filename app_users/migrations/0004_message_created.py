# Generated by Django 4.2.5 on 2023-09-29 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_alter_message_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

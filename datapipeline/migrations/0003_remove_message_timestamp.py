# Generated by Django 3.2.9 on 2023-11-27 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapipeline', '0002_user_assigned_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
    ]
# Generated by Django 3.2.9 on 2023-12-03 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapipeline', '0004_customgpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='customgpt',
            name='created_by',
            field=models.CharField(default='Sai', max_length=100),
        ),
        migrations.AddField(
            model_name='customgpt',
            name='university',
            field=models.CharField(default='UCSC', max_length=100),
        ),
    ]

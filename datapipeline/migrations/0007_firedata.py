# Generated by Django 4.2.7 on 2023-12-04 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapipeline', '0006_auto_20231204_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='FireData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
    ]

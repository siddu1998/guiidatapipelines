# Generated by Django 4.2.7 on 2023-12-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datapipeline", "0008_feedbackgpt_feedbackmessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="gpt_used",
            field=models.CharField(default="exit", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="sent_by",
            field=models.CharField(default="exit", max_length=20),
            preserve_default=False,
        ),
    ]
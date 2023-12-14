# Generated by Django 4.2.7 on 2023-12-14 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datapipeline", "0007_firedata"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackGPT",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("created_by", models.CharField(max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("instructions", models.TextField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_id", models.CharField(max_length=100)),
                ("student_id", models.CharField(max_length=100)),
                ("sent_by", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
                ("gpt_used", models.CharField(max_length=100)),
            ],
        ),
    ]
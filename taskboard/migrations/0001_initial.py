# Generated by Django 4.1.2 on 2022-10-12 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Doing", "Doing"),
                            ("Done", "Done"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "board_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="taskboard.board",
                    ),
                ),
            ],
        ),
    ]

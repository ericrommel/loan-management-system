# Generated by Django 2.2 on 2019-05-05 00:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="amount")),
                ("term", models.IntegerField(verbose_name="term")),
                ("rate", models.FloatField(verbose_name="rate")),
                ("date", models.DateTimeField(verbose_name="date")),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "payment",
                    models.CharField(
                        choices=[("made", "made"), ("missed", "missed")],
                        default="missed",
                        max_length=20,
                        verbose_name="payment",
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="date")),
                ("amount", models.FloatField(verbose_name="amount")),
                (
                    "loan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.Loan",
                        verbose_name="loan",
                    ),
                ),
            ],
        ),
    ]

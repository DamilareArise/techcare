# Generated by Django 4.2.4 on 2023-08-25 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("serviceapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="service_option",
            field=models.CharField(
                choices=[
                    ("Emergency Care", "Emergency Care"),
                    ("Ambulance service", "Ambulance service"),
                    ("Medicine & Pharmacy", "Medicine & Pharmacy"),
                    ("Operation & Surgery", "Operation & Surgery"),
                    ("Blood Testing", "Blood Testing"),
                    ("Outdoor Checkup", "Outdoor Checkup"),
                    ("General Health", "General Health"),
                    ("Cardiology", "Cardiology"),
                    ("Dental", "Dental"),
                    ("Neurology", "Neurology"),
                    ("Orthopaedics", "Orthopaedics"),
                ],
                max_length=20,
                unique=True,
            ),
        ),
        migrations.CreateModel(
            name="BookingService",
            fields=[
                ("booking_id", models.AutoField(primary_key=True, serialize=False)),
                ("service_option", models.IntegerField()),
                ("date_created", models.DateField(auto_now_add=True)),
                ("approved_date", models.DateField(blank=True, null=True)),
                ("approved_time", models.TimeField(blank=True, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("payment", models.BooleanField(blank=True, default=False, null=True)),
                ("served", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "patient_status",
                    models.CharField(
                        choices=[
                            ("unknown", "unknown"),
                            ("Booked for test", "Booked for test"),
                            ("Transferred", "Transferred"),
                            ("Admitted", "Admitted"),
                            ("Discharged", "Discharged"),
                            ("Dead", "Dead"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "doctor_remark",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("price", models.BigIntegerField(default=0)),
                (
                    "consultant_doctor",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consultant_doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hod",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hod",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "resident_doctor",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resident_doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

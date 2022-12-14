# Generated by Django 4.1.1 on 2022-09-27 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(default="", max_length=255, unique=True)),
                ("nickname", models.CharField(default="", max_length=100, unique=True)),
                ("gender", models.CharField(default="", max_length=100)),
                ("birth", models.IntegerField(default=0)),
                ("profile_image_id", models.IntegerField(blank=True, default=0)),
                ("liked_thumbnail", models.CharField(max_length=100)),
                ("resigned_time", models.DateTimeField(blank=True, null=True)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Member_View_Webtoons",
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
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_viewed_webtoons",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "accounts_member_view_webtoons",
                "ordering": ["-id"],
            },
        ),
    ]

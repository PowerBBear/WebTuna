# Generated by Django 4.1.1 on 2022-09-27 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webtoons", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webtoon",
            name="rating",
            field=models.FloatField(default=0),
        ),
    ]

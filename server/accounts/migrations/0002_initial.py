# Generated by Django 4.1.1 on 2022-09-27 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("webtoons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="member_view_webtoons",
            name="webtoon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="webtoons.webtoon"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="liked_webtoons",
            field=models.ManyToManyField(
                related_name="liked_webtoon_users", to="webtoons.webtoon"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="tags",
            field=models.ManyToManyField(related_name="tag_users", to="webtoons.tag"),
        ),
        migrations.AddField(
            model_name="member",
            name="view_webtoons",
            field=models.ManyToManyField(
                through="accounts.Member_View_Webtoons", to="webtoons.webtoon"
            ),
        ),
    ]
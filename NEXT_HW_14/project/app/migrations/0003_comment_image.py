# Generated by Django 5.0.4 on 2024-05-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_post_last_viewed_post_last_viewer_alter_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="comments/"),
        ),
    ]
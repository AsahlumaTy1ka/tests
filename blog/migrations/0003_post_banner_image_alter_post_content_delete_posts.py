# Generated by Django 5.0.6 on 2024-06-16 01:54

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="banner_image",
            field=models.ImageField(blank=True, null=True, upload_to="banners/"),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.DeleteModel(
            name="posts",
        ),
    ]
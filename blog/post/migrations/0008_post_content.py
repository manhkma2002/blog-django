# Generated by Django 3.2.7 on 2021-10-05 14:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
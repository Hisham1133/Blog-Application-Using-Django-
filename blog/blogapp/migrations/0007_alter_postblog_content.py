# Generated by Django 3.2.9 on 2021-12-21 13:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_postblog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

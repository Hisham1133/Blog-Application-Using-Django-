# Generated by Django 3.2.9 on 2021-12-14 10:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0005_alter_postblog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
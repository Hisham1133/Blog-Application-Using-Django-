# Generated by Django 3.2.9 on 2021-12-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_alter_postblog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='blog_header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

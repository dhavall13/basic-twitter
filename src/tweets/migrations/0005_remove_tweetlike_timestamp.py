# Generated by Django 2.2 on 2020-10-07 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20201007_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetlike',
            name='timestamp',
        ),
    ]

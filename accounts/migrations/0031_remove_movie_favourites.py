# Generated by Django 3.2.7 on 2021-10-23 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='favourites',
        ),
    ]
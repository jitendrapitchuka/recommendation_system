# Generated by Django 3.2.7 on 2021-10-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20211023_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='favourite',
            field=models.ManyToManyField(related_name='favourite', to='accounts.User'),
        ),
    ]

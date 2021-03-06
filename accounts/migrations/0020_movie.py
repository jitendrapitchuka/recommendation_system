# Generated by Django 3.2.7 on 2021-10-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('genres', models.CharField(max_length=130)),
                ('imdb_id', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('Image_url', models.URLField()),
                ('text', models.TextField(max_length=400)),
            ],
        ),
    ]

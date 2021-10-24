# Generated by Django 3.2.7 on 2021-10-23 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_remove_movie_favourites'),
    ]

    operations = [
        migrations.CreateModel(
            name='fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
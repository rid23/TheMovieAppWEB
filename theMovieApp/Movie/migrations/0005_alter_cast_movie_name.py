# Generated by Django 4.1.7 on 2023-03-15 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0004_cast_movie_name_alter_cast_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='Movie_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movie', to='Movie.movie'),
        ),
    ]

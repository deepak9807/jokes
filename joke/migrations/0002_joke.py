# Generated by Django 2.0 on 2018-04-28 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Title of joke')),
                ('joke', models.CharField(max_length=1000, verbose_name='Joke story')),
                ('keywords', models.CharField(max_length=50, verbose_name='Keywords of joke')),
                ('rating', models.IntegerField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(default='joke', on_delete=django.db.models.deletion.CASCADE, to='joke.Category')),
                ('language', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='joke.Language')),
            ],
        ),
    ]

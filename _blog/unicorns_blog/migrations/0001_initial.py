# Generated by Django 2.0.5 on 2018-05-28 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=150, verbose_name="Titre de l'article")),
                ('contenu', models.CharField(max_length=50, verbose_name="Contenu de l'article")),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de publication')),
                ('picture', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['date_publication', 'article_id'],
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
    ]

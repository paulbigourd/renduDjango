
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categorie(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50, verbose_name='Titre de l\'article')
    contenu = models.TextField(max_length=2000, verbose_name='Contenu de l\'article')
    date_publication= models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    picture = models.ImageField(upload_to='images', verbose_name='Image')
    slug = models.SlugField()
    categorie = models.ManyToManyField(Categorie)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['date_publication','article_id']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

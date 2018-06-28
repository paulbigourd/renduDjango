from django.contrib import admin
from unicorns_blog.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', )
    search_fields = ('titre',)
    list_filter = ('categorie',)

admin.site.register(Article, ArticleAdmin)
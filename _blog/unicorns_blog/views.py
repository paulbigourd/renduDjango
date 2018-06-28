from unicorns_blog.models import Article, Categorie
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    list_articles = Article.objects.all().order_by('date_publication')
    paginator = Paginator(list_articles, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'index.html', {'articles': articles})

def articles(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles.html', {'article': article})

def propos(request):
    return render(request, 'propos.html', {})


def recherche(request):
    query = request.GET.get('q')
    if query:
        resultats = Article.objects.filter(Q(title__icontains = query) | Q(content__icontains = query))
    else:
        resultats = Article.objects.all()

    nbresultats = results.count()
    context = {
        'items' : results,
        'nb_results' : nb_results,
        'query_search' : query,
    }

    return render(request, 'recherche.html', context)

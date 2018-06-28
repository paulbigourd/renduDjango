from django.urls import path
from unicorns_blog import views

app_name = 'unicorns_blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<slug:slug>/', views.articles, name='articles'),
    path('propos', views.propos, name='propos'),
]

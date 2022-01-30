from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index,name="index"),
    path('', views.BookListView.as_view(), name='article-list'),
    path('search-results', views.search_result),
]
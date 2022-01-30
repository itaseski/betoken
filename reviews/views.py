from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Book, Review

class BookListView(ListView):
    model = Book
    #template_name = "reviews/book_list.html"
    context_object_name = 'books'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def index(request):
    return render(request, 'reviews/index.html')

def search_result(request):
    context= {
        'search_result': request.GET.get("search", "There is only one match!")
    }
    return render(request, 'reviews/search_results.html', context)


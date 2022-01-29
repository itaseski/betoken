from django.shortcuts import render


def index(request):
    return render(request, 'reviews/index.html')

def search_result(request):
    context= {
        'search_result': request.GET.get("search", "There is only one match!")
    }
    return render(request, 'reviews/search_results.html', context)


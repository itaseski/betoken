from django.shortcuts import render


def index(request):
    return render(request, 'reviews/base.html')


from django.contrib import admin
from .models import Book, Publisher, Contributor, BookContributor, Review

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)

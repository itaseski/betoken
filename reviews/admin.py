from django.contrib import admin
from django.contrib.admin import AdminSite


from .models import Book, Publisher, Contributor, BookContributor, Review

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')
#admin_site.register(MyModel)




admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)

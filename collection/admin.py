from django.contrib import admin

from collection.models import Books

class BooksAdmin(admin.ModelAdmin):
    model = Books
    list_display = ('title', 'author', 'description', 'date', 'URL')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Books, BooksAdmin)
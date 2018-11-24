from django.shortcuts import render


def index(request):
    book = "Book title"
    return render(request, 'index.html', {
    'book': book,
    })

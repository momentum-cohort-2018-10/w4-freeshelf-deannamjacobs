from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from collection.models import Book



class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'initial_data', 'dogs.csv')) as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    description=row['description'],
                    date=row['date'],
                    URL=row['URL'],
                )
                book.save()
        print("Dogs loaded!")
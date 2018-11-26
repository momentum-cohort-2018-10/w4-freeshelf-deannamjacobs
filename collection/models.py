from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    URL = models.URLField()
    slug = models.SlugField(unique=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Book, self).save()




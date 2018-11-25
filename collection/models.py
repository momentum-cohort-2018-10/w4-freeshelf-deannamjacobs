from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    URL = models.URLField()
    slug = models.SlugField(unique=True)




from django.db import models
from django.utils import timezone


class BookLibrary(models.Model):
    class Meta:
        db_table = 'book_library'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    about = models.TextField()
    category = models.CharField(max_length=10)
    author = models.CharField(max_length=500)
    published_at = models.DateTimeField(default=timezone.now)

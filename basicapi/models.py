from django.db import models
import uuid
# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    coutry = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_year = models.CharField(max_length=100)
    genre = models.TextField(max_length=100)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + "_" + self.pub_year


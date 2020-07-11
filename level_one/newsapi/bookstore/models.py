from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='stores')

    def __str__(self):
        return self.name

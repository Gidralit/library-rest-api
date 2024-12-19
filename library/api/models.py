from multiprocessing.managers import Value
from random import choice, choices

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    year = models.IntegerField(
        unique=True,
        validators = [
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    GENRE_CHOICES = [
        ('document', 'Документ'),
        ('textbook', 'Учебник'),
        ('fantasy', 'Фэнтэзи'),
        ('mystery', 'Мистика'),
        ('historical', 'История'),
    ]
    genre = models.CharField(max_length=100, choices = GENRE_CHOICES)
    category = models.CharField(max_length=100)
    publishing_house = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.FileField(upload_to='files/', blank=True, null=True)

    class Meta:
        unique_together = ('name', 'year', 'publishing_house', 'author')

    def __str__(self):
        return self.name

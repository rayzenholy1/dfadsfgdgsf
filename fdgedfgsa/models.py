from django.db import models
from django.contrib.auth.models import User

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    registration_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    style = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    current_reader = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books')
    
    @property
    def is_available(self):
        return self.current_reader is None
    
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    duration = models.IntegerField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
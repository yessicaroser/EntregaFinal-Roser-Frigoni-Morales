from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    mail = models.CharField(max_length=70)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.titulo
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_at = models.DateTimeField(auto_created=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo
    

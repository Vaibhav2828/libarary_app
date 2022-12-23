from django.db import models

# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    author = models.CharField(max_length=50,default='anonymus')
    email = models.EmailField()
    describe = models.TextField(default='Performing CURD operation')

    def __str__(self):
        return self.name
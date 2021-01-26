from django.db import models
from django.conf import settings

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(category)
    publish_date = models.DateTimeField()
    views = models.IntegerField(default = 0)
    reviewed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=100)
    typeof = models.CharField(max_length=100)
    taste = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
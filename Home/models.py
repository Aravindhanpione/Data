from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50, primary_key = True, blank = True, default = None)

class Puja(models.Model):
    name = models.CharField(max_length=30, primary_key = True, blank = True, default = None)
    img = models.ImageField(upload_to = "PujaServices", null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class PujaDetails(models.Model):
    name = models.OneToOneField(Puja, on_delete=models.CASCADE, null = True)
    detailOffering = models.TextField(null = True)
    recommendedTemple = models.TextField(null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    

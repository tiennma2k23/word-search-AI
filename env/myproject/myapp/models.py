from django.db import models

#database

# Create your models here.
class Feature(models.Model): # convert tất cả thành phần trong Feature class vào Model
    name: models.CharField(max_length=100)
    details: models.CharField(max_length=500)
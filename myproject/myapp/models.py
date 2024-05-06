from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.TextField
    # allow user upload their avatars
    profile_image = models.ImageField(upload_to='avatars/', blank=True) # save avatar
    
# model to save PDF history
class PDFHistory(models.Model):
    # reference to the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pdf_histories')
    # FileField to storage the pdf
    pdf = models.FileField(upload_to='', blank=True)
    # store image
    image = models.ImageField(upload_to='', null=True, blank=True)


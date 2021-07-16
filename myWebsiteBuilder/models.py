from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class websiteDetail(models.Model):
    category = models.CharField(max_length=50)
    websiteName = models.CharField(max_length=100)
    homepageContent = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.category +' | '+ self.websiteName

class socialLink(models.Model):
    fbLink = models.CharField( max_length=250,blank=True, null=True)
    twittterLink = models.CharField(max_length=250,blank=True, null=True)
    googleLink = models.CharField(max_length=250,blank=True, null=True)
    gitLink  = models.CharField(max_length=250,blank=True, null=True)
    linkedinLink = models.CharField(max_length=250,blank=True, null=True)
    InstaLink = models.CharField(max_length=250,blank=True, null=True)

class aboutMe(models.Model):
    title = models.CharField( max_length=100)
    body = models.TextField()

class contactForm(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)
    phone = models.CharField(max_length=12)
    sender = models.EmailField()

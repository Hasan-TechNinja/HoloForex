from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class About_Us(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=800)
    about_image = models.ImageField(upload_to='about')
    mission = HTMLField()
    mission_image = models.ImageField(upload_to='mission')
    vision = HTMLField()
    we_offer = models.CharField(max_length=500)
    why_choose = models.TextField()
    choose_image = models.ImageField(upload_to='WhyChoose')
    
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=800)
    about_image = models.ImageField(upload_to='about')
    mission = HTMLField()
    mission_image = models.ImageField(upload_to='mission')
    vision = HTMLField()
    we_offer = models.CharField(max_length=500)
    why_choose = models.TextField()
    choose_image = models.ImageField(upload_to='WhyChoose')

    def __str__(self):
        return self.name
    

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="category", blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Blog', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    description = HTMLField()
    date = models.DateTimeField(auto_now=True)
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogs')
    comment = models.TextField(max_length=800)

    def __str__(self):
        return f"{self.blog.title}s Review"
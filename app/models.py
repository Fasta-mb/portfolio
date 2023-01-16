from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    title = models.CharField(max_length=120)
    link = models.URLField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.URLField(unique=True, null=True, blank=True)
    linkedin = models.URLField(unique=True, null=True, blank=True)
    github = models.URLField(unique=True, null=True, blank=True)
    instagram = models.URLField(unique=True, null=True, blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project = models.ManyToManyField(Project, blank=True)
    contact = models.OneToOneField(Contact, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    

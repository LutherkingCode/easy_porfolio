from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Design'),
        ('programming', 'Programming'),
        ('fitness', 'Fitness'),
        ('health', 'Health'),
        
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects_images/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title

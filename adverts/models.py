from django.db import models
from django.contrib.auth.models import User


class Adverts(models.Model):
    """
    Advert model, relating to 'owner'.
    Has default image set, so there is always a reference image.url. 
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    age = models.CharField(max_length=255, blank=True)
    breed = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=255, blank=True)
    children = models.CharField(max_length=255, blank=True)
    other_animals = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_advert_xeejcr',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.id} {self.title}"

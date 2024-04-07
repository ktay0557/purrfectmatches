from django.db import models
from django.contrib.auth.models import User
from adverts.models import Adverts


class Comment(models.Model):
    """
    Comment model, related to User and Adverts
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

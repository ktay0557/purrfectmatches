from django.db import models
from django.contrib.auth.models import User
from adverts.models import Adverts


class Likes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(
        Adverts, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'advert']

    def __str__(self):
        return f'{self.owner} {self.advert}'

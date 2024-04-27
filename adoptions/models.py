from django.db import models
from django.contrib.auth.models import User
from adverts.models import Adverts


class Adoption(models.Model):
    """
    Adoption model, related to User and Adverts
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.advert}'

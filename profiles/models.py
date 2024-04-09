from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    location = models.TextField(blank=True)
    previously_owned = models.CharField(max_length=255, blank=True)
    currently_own = models.TextField(blank=True)
    relationship_status = models.CharField(max_length=255, blank=True)
    children = models.CharField(max_length=255, blank=True)
    housing = models.CharField(max_length=255, blank=True)
    hobbies = models.TextField(blank=True)
    preferred_breed = models.CharField(max_length=255, blank=True)
    preferred_age = models.CharField(max_length=255, blank=True)
    preferred_sex = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_htuvfk'
    )
    is_staff = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
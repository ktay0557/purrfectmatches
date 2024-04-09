from django.db import models


class About(models.Model):
    """
    About model, for staff to keep info updated.
    Has default image set, so there is always a reference image.url. 
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_advert_xeejcr',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title}"

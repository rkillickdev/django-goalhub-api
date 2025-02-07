from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL  # "auth.User"


# Create your models here.
class Team(models.Model):
    """Team Model"""

    user = models.ForeignKey(
        User, default=None, null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

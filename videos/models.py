from django.db import models
from django.contrib.auth import get_user_model

class Video(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

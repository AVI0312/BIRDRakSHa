# api/models.py

from django.db import models

class BirdImage(models.Model):
    image = models.ImageField(upload_to='bird_images/')
    predicted_class = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.predicted_class} - {self.image.name}"

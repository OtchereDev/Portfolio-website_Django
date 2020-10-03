from django.db import models

class blog(models.Model):
    Title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    images = models.ImageField(upload_to='images/')
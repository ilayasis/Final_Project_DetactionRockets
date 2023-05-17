from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files')
    filename = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', null=True, blank=True)
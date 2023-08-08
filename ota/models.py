from django.db import models

# Create your models here.

class Firmware(models.Model):
    version = models.CharField(max_length=20)
    file = models.FileField(upload_to='firmwares/')
    description = models.TextField()
    
    class Meta:
        app_label = 'ota'

    def __str__(self):
        return self.version

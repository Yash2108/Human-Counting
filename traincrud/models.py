from django.db import models
from django.db.models import Model
from .validators import file_size


class Train(models.Model):

    TrainImage = models.ImageField(upload_to ='images/')
    OutputImage = models.CharField(max_length = 100)
   
class Video(models.Model):
    video=models.FileField(upload_to="video/",validators=[file_size])
   
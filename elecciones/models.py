from django.db import models

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Candidato(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    candidato_name = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
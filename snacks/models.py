from django.db import models

class Snack(models.Model):
    name = models.CharField(max_length=256)
    

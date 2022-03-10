from django.db import models

# Create your models here.


class links(models.Model):
	key = models.CharField(max_length=8)
	value = models.CharField(max_length=100)
	
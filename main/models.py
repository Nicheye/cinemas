from django.db import models

# Create your models here.

class Cinema(models.Model):
	title = models.CharField(max_length=52)
	location = models.CharField(max_length=61)
	street = models.CharField(max_length=52)
	ur_name = models.CharField(max_length=100)
	website = models.CharField(max_length=500,blank=True,null=True)
	inn = models.CharField(max_length=10)
	map = models.CharField(max_length=250)
	def __str__(self) -> str:
		return self.title
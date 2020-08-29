from django.db import models

# Create your models here.
class Tweet(models.Model):
	tag = models.CharField(max_length=100, default = "")
	text = models.CharField(max_length=1000,default = "")

	def publish(self):
		self.save()

	def __str__(self):
		return self.text
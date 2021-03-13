from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	banner = models.ImageField(upload_to='banners', default='default.png')
	title = models.CharField(max_length=60, unique=True)
	author = models.CharField(max_length=60)
	dop = models.DateField(verbose_name="Date of Publication")
	content = models.TextField(blank=True)
	def __str__(self):
		return self.title
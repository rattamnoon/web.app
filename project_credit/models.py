from django.db import models

class credit(models.Model):
	credit_name = models.CharField(max_length=200)
	credit_price = models.CharField(max_length=200)
	credit_detail = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.credit_name

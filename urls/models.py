from django.db import models

# Create your models here.
class Link(models.Model):
	name=models.CharField(max_length=300)
	url=models.URLField()
	current_price=models.FloatField(blank=True)
	old_price=models.FloatField(default=0)
	price_different=models.FloatField(default=0)
	updated=models.DateTimeField(auto_now=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)
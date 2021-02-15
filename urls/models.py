from django.db import models
from .utils import get_urls_data
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

	class Meta:
		ordering=('price_different','-created')

	def save(self,*args,**kwargs):
		name,price=get_urls_data(self.url)

		if self.current_price :
			if price !=old_price:
				diff = price-old_price
				self.price_different=round(diff,2)
				self.old_price=old_price
		else:
			self.current_price=0
			self.price_different=0


		self.name=name
		self.current_price=price
		super().save(*args,**kwargs)

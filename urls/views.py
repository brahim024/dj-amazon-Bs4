from django.shortcuts import render
from .form import AddLinkForm
from .models import Link
# Create your views here.
 
# qs
# number of item
# number of items discounted
# form
# error(if exist urls)

def home(request):
	nb_discounted=0   # number of discounted
	error=None

	form=AddLinkForm(request.POST or None)
	if request.method='POST':
		try:
			if form.is_valid:
				form.save()

		except AttributeError:
			error='Ups could get the name or price'
		except:
			error='Ups somthing went wrong!'
	else:
		form=AddLinkForm()


	qs=Link.objects.all()
	item_no=qs.count()  # item number

	if item_no >0:
		discount_list=[]
		for item in qs:
			if item.old_price > item.current_price:
				discount_list.append(item)
			nb_discounted=len(discount_list)
	context={
		'qs':qs,
		'item_no':item_no,
		'form':form,
		'error':error,
		'nb_discounted':nb_discounted
	}
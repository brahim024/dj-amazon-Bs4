from django.shortcuts import render
from .form import AddLinkForm
# Create your views here.
 
# qs
# number of item
# number of items discounted
# form
# error(if exist urls)

def home(request):
	no_discounted=0
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
from django.shortcuts import render
from .models import Block, Category, Contacts

def home(request):
	cteg = Category.objects.all().order_by('idsort')
	exper = Block.objects.all().order_by('idsort')
	conts = Contacts.objects.all().order_by('idsort')

	return render(request, 'idx/data.html', {'conts':conts, 'cteg':cteg, 'exper':exper})


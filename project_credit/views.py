from django.shortcuts import render
from django.http import HttpResponse
from .models import credit

def Home(request):
	return render(request, 'home.html')

def About(request):
	return render(request, 'about.html')

def Credit_Home(request):
	Credit = credit.objects.all()
	context = {'Credit':Credit}
	return render(request, 'credit_home.html', context)

# -*- coding: utf 8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Mozix
#(datapublicacao__gt=timezone.now().date() - timedelta(days=-7))
def index(request):
	mozis = Mozix.objects.filter(tipos='UNICA', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'mozi/index.html', {'mozis': mozis})	

def post_detail(request, pk):
    post = get_object_or_404(Mozix, pk=pk)
    Mozix.objects.get(pk=pk)
    return render(request, 'mozi/post_detail.html', {'post': post})

def doces(request):
	mozis = Mozix.objects.filter(tipos='COMIDA')
	#mozis = Mozix.objects.filter(tipos='COMIDA')
	return render(request, 'mozi/index.html', {'mozis': mozis})

def bebidas(request):
	mozis = Mozix.objects.filter(tipos='REFRI')
	return render(request, 'mozi/index.html', {'mozis': mozis})
	
def petiscos(request):
	mozis = Mozix.objects.filter(tipos='PETI')
	return render(request, 'mozi/index.html', {'mozis': mozis})

def salgados(request):
	mozis = Mozix.objects.filter(tipos='SALG')
	return render(request, 'mozi/index.html', {'mozis': mozis})

def assados(request):
	mozis = Mozix.objects.filter(tipos='ASSA')
	return render(request, 'mozi/index.html', {'mozis': mozis})

#modificacao



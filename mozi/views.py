# -*- coding: utf 8 -*-
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Mozix

def index(request):
	objetos = Mozix.objects.filter(tipos='UNICO', datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'mozi/index.html', {'objetos': objetos})	

def post_detail(request, pk):
    post = get_object_or_404(Mozix, pk=pk)
    Mozix.objects.get(pk=pk)
    return render(request, 'mozi/post_detail.html', {'post': post})

def doces(request):
	objetos = Mozix.objects.filter(tipos='DOCE')
	return render(request, 'mozi/index.html', {'objetos': objetos})

def bebidas(request):
	objetos = Mozix.objects.filter(tipos='REFRI')
	return render(request, 'mozi/index.html', {'objetos': objetos})
	
def petiscos(request):
	objetos = Mozix.objects.filter(tipos='PETI')
	return render(request, 'mozi/index.html', {'objetos': objetos})

def salgados(request):
	objetos = Mozix.objects.filter(tipos='SALG')
	return render(request, 'mozi/index.html', {'objetos': objetos})

def assados(request):
	objetos = Mozix.objects.filter(tipos='ASSA')
	return render(request, 'mozi/index.html', {'objetos': objetos})

#modificacao



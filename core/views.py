import datetime
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Promocao
from mozi.models import Mozix
from pet.models import Petmania

def index(request):
	posts = Promocao.objects.filter(validade__lte=timezone.now()).order_by('-validade')
	mozis = Mozix.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))#usar o filtro manipulando o timezone é uma boa, exibir valores postados na ultima semana
	petmanias = Petmania.objects.filter(datapublicacao__gt=timezone.now().date() - timedelta(days=7))
	return render(request, 'core/index.html', {'posts': posts, 'mozis': mozis, 'petmanias': petmanias})

def vital(request):
	return render(request, 'core/vital.html', {})

def bairro(request):
	return render(request, 'core/bairro.html', {})

def centro(request):
	return render(request, 'core/centro.html', {})

def domlucio(request):
	return render(request, 'core/domlucio.html', {})

def facaparte(request):
	return render(request, 'core/facaparte.html', {})
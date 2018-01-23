from django.shortcuts import render
from django.utils import timezone
from .models import Promocao


def index(request):
	posts = Promocao.objects.filter(validade__lte=timezone.now()).order_by('-validade')
	return render(request, 'core/index.html', {'posts': posts})

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
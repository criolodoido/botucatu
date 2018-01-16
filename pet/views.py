from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Petmania

def petmania(request):
	objetos = Petmania.objects.filter(datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'pet/index.html', {'objetos': objetos})	

def post_detail(request, pk):
    post = get_object_or_404(Petmania, pk=pk)
    Petmania.objects.get(pk=pk)
    return render(request, 'pet/post_detail.html', {'post': post})

def comida(request):
	objetos = Petmania.objects.filter(tipos='COMER')
	return render(request, 'pet/index.html', {'objetos': objetos})

def educacao(request):
	objetos = Petmania.objects.filter(tipos='EDUCA')
	return render(request, 'pet/index.html', {'objetos': objetos})
	
def acessorios(request):
	objetos = Petmania.objects.filter(tipos='ACESS')
	return render(request, 'pet/index.html', {'objetos': objetos})

def higiene(request):
	objetos = Petmania.objects.filter(tipos='HIGI')
	return render(request, 'pet/index.html', {'objetos': objetos})


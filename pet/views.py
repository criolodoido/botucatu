from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Petmania

def petmania(request):
	petmanias = Petmania.objects.filter(datapublicacao__lte=timezone.now()).order_by('-datapublicacao')
	return render(request, 'pet/index.html', {'petmanias': petmanias})	

def post_detail(request, pk):
    post = get_object_or_404(Petmania, pk=pk)
    Petmania.objects.get(pk=pk)
    return render(request, 'pet/post_detail.html', {'post': post})

def comida(request):
	petmanias = Petmania.objects.filter(tipos='COMER')
	return render(request, 'pet/index.html', {'petmanias': petmanias})

def educacao(request):
	petmanias = Petmania.objects.filter(tipos='EDUCA')
	return render(request, 'pet/index.html', {'petmanias': petmanias})
	
def acessorios(request):
	petmanias = Petmania.objects.filter(tipos='ACESS')
	return render(request, 'pet/index.html', {'petmanias': petmanias})

def higiene(request):
	petmanias = Petmania.objects.filter(tipos='HIGI')
	return render(request, 'pet/index.html', {'petmanias': petmanias})


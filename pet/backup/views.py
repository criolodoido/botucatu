from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Petmania

def petmania(request):
	objetos = Petmania.objects.filter(datapublicacao__lte=timezone.now()).order_by('datapublicacao')
	return render(request, 'pet/index.html', {'objetos': objetos})	

def post_detail(request, pk):
    objeto = get_object_or_404(Petmania, pk=pk)
    Petmania.objects.get(pk=pk)
    return render(request, 'pet/post_detail.html', {'objeto': objeto})

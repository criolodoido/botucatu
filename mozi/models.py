# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Mozix(models.Model):
	TIPOS = (
		('DOCE', 'Comidas'),
		('REFRI', 'Bebidas'),
		('PETI', 'Petiscos'),
		('SALG', 'Salgados'),
		('ASSA', 'Assados'),
	)

	tipos = models.CharField(max_length=6, choices=TIPOS, null=False)
	titulo = models.CharField(max_length=100, null=False, blank=False)
	apresentacao = models.TextField()
	imagem = CloudinaryField('imagem', null=False, blank=False)
	datapublicacao = models.DateTimeField(null=False, blank=False)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		#return reverse("detalhe", kwargs={"pk": self.pk})
		return "post/%s" %(self.pk)
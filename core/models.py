from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Promocao(models.Model):
	nome = models.CharField(max_length=200, null=False, blank=False)
	apresentacao = models.TextField(null=False, blank=False)
	foto = CloudinaryField('foto', null=True, blank=True)
	postado = models.DateTimeField(
            default=timezone.now)
	validade = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.postado = timezone.now()
		self.save()

	def __str__(self):
		return self.nome
from django.db import models
from django.utils import timezone

class Referencia(models.Model):
    creador_referencia = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre_referencia = models.CharField(max_length=200)
    observaciones = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def Publicacion(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

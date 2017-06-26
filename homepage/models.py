from django.db import models

from multiselectfield import MultiSelectField
from django.utils import timezone
from django.utils.formats import get_format
from django.contrib.auth.models import User


class Favoritos(models.Model):
    id = models.AutoField(primary_key=True)
    idAlumno = models.IntegerField()
    idVendedor = models.IntegerField()

    def __str__(self):
        return self.idAlumno

    class Meta:
        db_table = 'Favoritos'


class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='avatars')

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'imagen'


class Transacciones(models.Model):
    my_formats = get_format('DATETIME_INPUT_FORMATS')
    idTransaccion = models.AutoField(primary_key=True)
    nombreComida = models.CharField(max_length=200, blank=True, null=True)
    idVendedor = models.IntegerField()
    precio = models.IntegerField()
    fechaAhora = str(timezone.now()).split(' ', 1)[0]
    fecha = models.CharField(max_length=200, default=fechaAhora)

    def __str__(self):
        return str(self.idTransaccion)

    class Meta:
        db_table = 'transacciones'

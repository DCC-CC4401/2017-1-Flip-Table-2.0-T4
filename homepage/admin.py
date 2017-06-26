from django.contrib import admin

from .models import Imagen
from .models import Transacciones

admin.site.register(Imagen)
admin.site.register(Transacciones)

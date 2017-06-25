from django.contrib import admin

from .models import Usuario
from .models import Comida
from .models import Imagen
from .models import Transacciones
from account.models import Client, Peddler, Established

admin.site.register(Usuario)
admin.site.register(Comida)
admin.site.register(Imagen)
admin.site.register(Transacciones)

admin.site.register(Client)
admin.site.register(Peddler)
admin.site.register(Established)


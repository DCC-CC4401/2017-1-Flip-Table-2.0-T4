from django.contrib import admin

from account.models import Client, Peddler, Established

admin.site.register(Client)
admin.site.register(Peddler)
admin.site.register(Established)

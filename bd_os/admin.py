from django.contrib import admin

from .models import *
admin.site.register(OS)

admin.site.register(EQUIPAMENTO)
admin.site.register(MARCA)
admin.site.register(TECNICO)
admin.site.register(STATUS)
admin.site.register(CLIENTE)
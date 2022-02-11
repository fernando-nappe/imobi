from django.contrib import admin
from django.contrib.admin.helpers import AdminReadonlyField
from .models import DiasVisita, Visita, Imovel, Cidade, Imagem, Horario

admin.site.register(Cidade)
admin.site.register(Imovel)
admin.site.register(Imagem)
admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Visita)
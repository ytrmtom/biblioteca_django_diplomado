from django.contrib import admin
from .models import Categoria, Autor, Libro, Usuario, Prestamo

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamo)

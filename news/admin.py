from django.contrib import admin

# Register your models here.
from .models import Articolo, Giornalista
# Register your models here.

admin.site.register(Articolo)
admin.site.register(Giornalista)
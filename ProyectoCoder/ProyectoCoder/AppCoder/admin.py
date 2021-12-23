from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Donaciones)

admin.site.register(Rescatados)

admin.site.register(Adopciones)


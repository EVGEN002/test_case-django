from django.contrib import admin

# Register your models here.

from .models import Gender, Human

admin.site.register(Gender)
admin.site.register(Human)
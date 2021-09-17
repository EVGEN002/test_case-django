from django.contrib import admin

# Register your models here.

from .models import Gender, Match

admin.site.register(Gender)
admin.site.register(Match)
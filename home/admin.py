from django.contrib import admin

# Register your models here.
from .models import Grocerries, Meals

admin.site.register(Grocerries)
admin.site.register(Meals)
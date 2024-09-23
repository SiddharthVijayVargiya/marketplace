from django.contrib import admin

# Register your models here.
# marketplace/admin.py

from django.contrib import admin
from .models import Mango, TreeDetails, Order

admin.site.register(Mango)
admin.site.register(TreeDetails)
admin.site.register(Order)

# admin.py

from django.contrib import admin
from .models import TreeDetails

# Define a custom admin class
class TreeDetailsAdmin(admin.ModelAdmin):
    list_display = ['mango', 'location']  # Add 'location' to list_display

# Unregister the model first if it's already registered
admin.site.unregister(TreeDetails)

# Register the model with the custom admin class
admin.site.register(TreeDetails, TreeDetailsAdmin)

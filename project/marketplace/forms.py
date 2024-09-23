from django import forms
from .models import Mango, TreeDetails

class MangoForm(forms.ModelForm):
    class Meta:
        model = Mango
        fields = ['variety', 'quantity', 'images', 'video', 'taste_review']

class TreeDetailsForm(forms.ModelForm):
    class Meta:
        model = TreeDetails
        fields = ['location', 'country', 'state', 'city', 'address', 'age', 'variety', 'fertilizer_used', 'tree_images', 'pesticide_used', 'tree_video']


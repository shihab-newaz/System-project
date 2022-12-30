from django import forms
from django.forms import ModelForm
from .models import Review,Customer

class reviewForm(ModelForm):
    class Meta:
        model=Review
        fields = ('review','rating','product','customer',)

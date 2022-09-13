from dataclasses import field
from django import forms
from .models import Books
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	author = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = Books
		fields = ['name', 'author']

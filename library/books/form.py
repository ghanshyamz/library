from dataclasses import field
from django import forms
from .models import Books
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
	name = forms.CharField(required=True)
	author = forms.CharField(required=True)
	
	class Meta:
		model = Books
		fields = ['name', 'author']

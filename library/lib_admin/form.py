from dataclasses import field
from django import forms
from .models import LibAdmin
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
	lastname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
	class Meta:
		model = LibAdmin
		fields = ['firstname','lastname','email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.first_name = self.cleaned_data['firstname']
		user.last_name = self.cleaned_data['lastname']
		user.email = self.cleaned_data['email']
		user.username = user.email
		if commit:
			user.save()
		return user

class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = LibAdmin
        fields = ['email','password']
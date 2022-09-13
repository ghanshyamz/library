from dataclasses import field
from django import forms
from .models import LibAdmin
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	firstname = forms.CharField(required=True)
	lastname = forms.CharField(required=True)
	email = forms.EmailField(required=True)
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
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = LibAdmin
        fields = ['email','password']
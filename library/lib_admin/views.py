from django.shortcuts import render, redirect
from .form import UserLoginForm, UserRegisterForm
from django.contrib import auth
from books.models import Books

# Create your views here.
def home(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books':books})

def register(request):
    if request.method == 'POST':
        filled_form = UserRegisterForm(request.POST)
        if filled_form.is_valid():
            user = filled_form.save()
            message = 'Successfully Registered'
            auth.login(request, user)
            return redirect(to='home') 
        else:
            message = 'User already exist OR username is taken'
            new_form = UserRegisterForm()
            return render(request, 'signup.html',{'registration_form':new_form, 'message':message})
    else:
        form = UserRegisterForm()
        return render(request, 'signup.html',{'registration_form':form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            message = 'Login Failed'
            form = UserLoginForm()
            return render(request, 'login.html', {'login_form':form, 'message':message})
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'login_form':form, 'message':''})

def logout(request):
    auth.logout(request)
    return redirect('home')

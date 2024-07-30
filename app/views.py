from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
from django.contrib.auth import login as auth_login

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['username']
        password=request.POST['password']
        hash_pass=make_password(password=password)
        user = Users(name=name, email=email,password=hash_pass)
        user.save()
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        email=request.POST['username']
        password=request.POST['password']
        try:
            user=Users.objects.get(email=email)
            if check_password(password, user.password):
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'index.html', {'error': 'Invalid Password'})
        except Users.DoesNotExist:
            return render(request, 'index.html', {'error': 'Email does not exist'})
    else:
        return render(request, 'index.html')
    
def home_view(request):
    return render(request, 'landing.html')
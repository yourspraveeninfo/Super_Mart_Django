from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/inventory/products/')

    context = {"error": ""}

    if request.method == "POST":
        print(request.POST)

        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        print(user.role)

        if user is not None:
            login(request, user)
            
            if user.role == 0:
            
                return redirect('/orders/all/customers/')
        
            elif user.role == 1:
                
                return redirect('/inventory/products/')
            
            elif user.role == 2:
                
                return redirect('/orders/orders/')
                
        else:
            context["error"] = "* Invalid Username or Password !"

    return render(request, 'login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('/')

def SignupPage(request):
    context = {"error": ""}

    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email_address')
        age = request.POST.get('age')
        role = request.POST.get('role')
        password = request.POST.get('password')

        user_check = User.objects.filter(username=username)

        if user_check.exists():
            context["error"] = "* Username already exists!"
        else:
            new_user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age,
                role=role
            )
            new_user.set_password(password)
            new_user.save()

            return redirect('/')

    return render(request, 'signup.html', context)

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import User
from mongoengine.errors import NotUniqueError

# Create your views here.

def register(request):
    error_message = ''
    if request.method == 'POST': 
        ## passing all the information to the form 
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            try: 
                # saving the user 
                user = User(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                user.save() # this step will verify if the user already exists 
                return render(request, 'successful_registration.html')
            except NotUniqueError:
                error_message = "A user with this email or username already exists"

    form = RegisterForm() 
    
    return render(request, 'register.html', {'form' : form, 'error_message':error_message })


def success_view(request):
    return HttpResponse("Registration successful!!")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects(email=email).first()

        if user:
            if user.password == password: 
                print("Correct Password, Logging in..")
                return HttpResponse("Logged in..")
            else:
                print("Incorrect password")
                return render(request, 'login.html', {"error":"Incorrect Password"})
        else:
            print("User doesn't exist")
            return render(request, 'login.html', {"error":"User doesn't exist"})
    
    return render(request, 'login.html')
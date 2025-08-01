from django.shortcuts import render, redirect
from .models import *
from Library_manager import * 

def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        number = request.POST['number']

        New_user = register.objects.create(
            username=username,
            email=email,
            password=password, 
            number=number
        )

        # Set session variables
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password
        request.session['number'] = number

        return redirect('Library')  

    return render(request, 'register.html')

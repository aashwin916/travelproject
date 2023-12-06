from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def reg(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['Email']
        password = request.POST['Password']
        cpassword = request.POST['Password2']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return  redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return  redirect('reg')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')

            messages.info(request,'User created')

        else:
            messages.info(request,"password not matching")
            return redirect('reg')
        return redirect('/')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
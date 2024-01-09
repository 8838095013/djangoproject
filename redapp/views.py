from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from . models import UserProfile

def register(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        email = request.POST['email']

        if not UserProfile.objects.filter(username=username).exists() and not UserProfile.objects.filter(email=email).exists():
            UserProfile.objects.create(username=username, password=make_password(password), email=email)
            return redirect('login' ,permanent=True)
        else:
            return render(request, 'register.html', {"error": 'Username or email already exists'})
            
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        if UserProfile.objects.filter(username=username).exists():
            user = UserProfile.objects.get(username=username)
            print(user)
            request.session['username'] = username

            if check_password(password, user.password):
                return redirect('success')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        else:
            return render(request, 'login.html', {'error': 'Username does not Exist'})

    return render(request, 'login.html')

def dashboard(request):
    return render(request,"success.html",{'user':request.session['username']})        

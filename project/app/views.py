from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache


def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def plans(req):
    return render(req, 'plans.html')

def trainers(req):
    return render(req, 'trainers.html')

def problem(req):
    return render(req, 'problem.html')


def contact(req):
    return render(req, 'contact.html')

@never_cache
def sign(req):
    if req.method == "POST":
        uname = req.POST.get("username")
        email = req.POST.get("email")
        pass1 = req.POST.get("password1")
        pass2 = req.POST.get("password2")
        
        if pass1 != pass2:
            messages.error(req, "Passwords not matching!")
            return redirect('sign')

        if User.objects.filter(username=uname).exists():
            messages.error(req, "Username already exists!")
            return redirect('sign')

        User.objects.create_user(
            username=uname,
            email=email,
            password=pass1
        )

        messages.success(req, "Account created successfully!")
        return redirect('login')
    return render(req, 'sign.html')

@never_cache
def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")

        uname = uname.strip()
        user = User.objects.filter(username__iexact=uname).first()

        if not user:
            messages.error(request, "User not found! Please signup first.")
            return redirect('sign')

        if user.check_password(password):

            request.session['user_id'] = user.id
            request.session['username'] = user.username

            messages.success(request, "Login successful!")
            return redirect('home')

        else:
            messages.error(request, "Wrong password!")
            return redirect('login')

    return render(request, 'login.html')

@never_cache
def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully!")
    return redirect('login')
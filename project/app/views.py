from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from .models import report,con

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def plans(req):
    return render(req, 'plans.html')

def trainers(req):
    return render(req, 'trainers.html')

def problem(req):

    if req.method == "POST":

        name = req.POST.get("name")
        email = req.POST.get("email")
        problem= req.POST.get("problem")
        message = req.POST.get("message")

        report.objects.create(
            name=name,
            email=email,
            problem=problem,
            message=message
        )
        messages.success(req, "Problem Submitted Successfully!")
        return redirect('problem')
    return render(req, 'problem.html')


def contacts(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        phone=req.POST.get('phone')
        message=req.POST.get('message')
        
        con.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(req, "Contact Submitted Successfully!")
        return redirect('contacts')
        
    return render(req, 'contacts.html')

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

        # 🔥 HARD CODE ADMIN ADD (NEW ADDITION ONLY)
        if uname == "admin" and password == "admin123":
            request.session['admin'] = True
            request.session['username'] = "Admin"

            messages.success(request, "Admin login successful!")
            return redirect('adminpanel')

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

@never_cache
def adminpanel(req):
    return render (req,'adminpanel.html')

def reports(req):
    data = report.objects.all()
    return render(req, 'reports.html', {'data': data})

def contactlist(req):
    data=con.objects.all()
    return render(req,'contactlist.html',{'data':data})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

from .models import report, con, TrainerForm, Joined


# HOME PAGE
def home(req):
    return render(req, 'home.html')


# ABOUT PAGE
def about(req):
    return render(req, 'about.html')


# PLANS PAGE
def plans(req):
    return render(req, 'plans.html')


# TRAINERS PAGE
def trainers(req):

    if req.method == "POST":

        name = req.POST.get('name')
        age = req.POST.get('age')
        phone = req.POST.get('phone')
        trainer = req.POST.get('trainer')
        goal = req.POST.get('goal')
        message = req.POST.get('message')

        TrainerForm.objects.create(
            name=name,
            age=age,
            phone=phone,
            trainer=trainer,
            goal=goal,
            message=message
        )

        messages.success(req, "Your request sent successfully!")
        return redirect('trainers')

    return render(req, 'trainers.html')


# JOIN PAGE
def join(req):

    if req.method == "POST":

        name = req.POST.get("name")
        email = req.POST.get("email")
        phone = req.POST.get("phone")
        age = req.POST.get("age")
        plan = req.POST.get("plan")
        trainer = req.POST.get("trainer")
        goal = req.POST.get("goal")
        message = req.POST.get("message")

        Joined.objects.create(
            name=name,
            email=email,
            phone=phone,
            age=age,
            plan=plan,
            trainer=trainer,
            goal=goal,
            message=message
        )
        messages.success(req, "You joined successfully!")
        return redirect('join')

    return render(req, 'join.html')


# JOINING LIST PAGE
def joining(req):
    data = Joined.objects.all()
    return render(req,"joining.html", {'data':data})


# PROBLEM PAGE
def problem(req):

    if req.method == "POST":

        name = req.POST.get("name")
        email = req.POST.get("email")
        problem = req.POST.get("problem")
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


# CONTACT PAGE
def contacts(req):

    if req.method == "POST":

        name = req.POST.get('name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        message = req.POST.get('message')

        con.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(req, "Contact Submitted Successfully!")
        return redirect('contacts')

    return render(req, 'contacts.html')


# SIGNUP
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


# LOGIN
@never_cache
def login(request):

    if request.method == "POST":

        uname = request.POST.get("username")
        password = request.POST.get("password")

        uname = uname.strip()

        # ADMIN LOGIN
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


# LOGOUT
@never_cache
def logout(request):

    request.session.flush()

    messages.success(request, "Logged out successfully!")

    return redirect('login')


# ADMIN PANEL
@never_cache
def adminpanel(req):
    return render(req, 'adminpanel.html')


# REPORTS LIST
def reports(req):

    data = report.objects.all()

    return render(req, 'reports.html', {'data': data})


# CONTACT LIST
def contactlist(req):

    data = con.objects.all()

    return render(req, 'contactlist.html', {'data': data})


# TRAINING LIST
def training(req):

    data = TrainerForm.objects.all()

    return render(req, 'training.html', {'data': data})
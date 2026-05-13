from django.shortcuts import render ,redirect
from django.contrib import messages

# Create your views here.


def home(req):
    return render(req,'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # (demo check)
        if username == "admin" and password == "123":

            # 🔥 SESSION STORE
            request.session['username'] = username
            request.session['password'] = password   # (demo only)
            request.session['is_logged_in'] = True

            return redirect('home')

        else:
            return render(request, 'login.html', {'error': 'Invalid'})

    return render(request, 'login.html')
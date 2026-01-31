from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials or not an admin")

    return render(request, 'admin_login.html')


@login_required(login_url='admin_login')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')

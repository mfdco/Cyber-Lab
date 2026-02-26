from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .info import SignUpForm
from django.http import JsonResponse

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})

    
    
#Returns logged-in user's account info to URL's account.
def account_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not logged in"}, status=401)
    
    user = request.user
    return JsonResponse({
        "id": user.id,
        "username": user.username,
        "email": user.email,
    })
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        return render(request, "accounts/login.html", {"error": "Invalid username or password"})
    return render(request ,"accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

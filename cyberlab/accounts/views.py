from django.shortcuts import render, redirect
from django.contrib.auth import login
from .info import SignUpForm
from django.http import JsonResponse

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})
def login_view(request):
    return render(request, "accounts/login.html")

    
    
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
    
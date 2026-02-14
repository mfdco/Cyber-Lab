from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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
            print(f"User logged in: {user.username}")
            #change the account in the statement below to the html you make.
            return redirect("account")
        return render(request, "accounts/login.html", {"error": "Invalid username or password"})
    return render(request ,"accounts/login.html")

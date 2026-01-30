 from django.shortcuts import render
 from .info import SignUpForm

 def signup_view(request):
      created = False
      if request.method == "POST":
          form = SignUpForm(request.POST)
          if form.is_valid():
              form.save()
              created = True
              form = SignUpForm()
      else:
          form = SignUpForm()
      return render(request, "accounts/signup.html", {"form": form, "created": created})

  def login_view(request):
      return render(request, "accounts/login.html")
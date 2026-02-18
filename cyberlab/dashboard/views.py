from django.shortcuts import render, redirect


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard/dashboard.html', {'user': request.user})

from django.shortcuts import render, redirect
from challenges.models import Submission


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard/dashboard.html', {'user': request.user})


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard/profile.html', {'user': request.user})


def history_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    submissions = Submission.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'dashboard/history.html', {'user': request.user, 'submissions': submissions})

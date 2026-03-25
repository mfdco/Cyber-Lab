from django.shortcuts import render, redirect
from challenges.models import Submission, Problems
from itertools import groupby


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    problems = {p.id: p for p in Problems.objects.all()}

    solved_ids = set(
        Submission.objects.filter(user=request.user, correct=True)
        .values_list('problem_id', flat=True)
    )

    return render(request, 'dashboard/dashboard.html', {
        'user': request.user,
        'problems': problems,
        'solved_ids': solved_ids,
    })


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard/profile.html', {'user': request.user})


def progress_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    all_problems = Problems.objects.all().order_by('section', 'problem_number')

    solved_ids = set(
        Submission.objects.filter(user=request.user, correct=True)
        .values_list('problem_id', flat=True)
    )

    sections = {}
    for problem in all_problems:
        sec = problem.section or 'General'
        if sec not in sections:
            sections[sec] = []
        sections[sec].append({
            'problem': problem,
            'solved': problem.id in solved_ids,
        })

    total = all_problems.count()
    solved_count = len(solved_ids)
    percent = int((solved_count / total) * 100) if total > 0 else 0

    # SVG ring: r=64, circumference = 2 * pi * 64 ≈ 402
    circumference = 402
    dashoffset = round(circumference * (1 - percent / 100))

    return render(request, 'dashboard/progress.html', {
        'user': request.user,
        'sections': sections,
        'total': total,
        'solved_count': solved_count,
        'percent': percent,
        'circumference': circumference,
        'dashoffset': dashoffset,
    })

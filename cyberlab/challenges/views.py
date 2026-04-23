from django.shortcuts import render, redirect, get_object_or_404
from .models import Submission, Problems
from .grading import check_flag
from django.http import JsonResponse


def challenge_view(request, problem_id):
    if not request.user.is_authenticated:
        return redirect('login')

    problem = get_object_or_404(Problems, id=problem_id)
    result = None

    if request.method == "POST":
        submitted = request.POST.get("flag", "")
        correct = check_flag(submitted, problem.hashed_flags)

        Submission.objects.create(
            user=request.user,
            problem=problem,
            flag_submitted=submitted,
            correct=correct,
        )

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'result': 'correct' if correct else 'incorrect'})

        result = "correct" if correct else "incorrect"

    return render(request, 'challenges/challenge.html', {
        'user': request.user,
        'problem': problem,
        'result': result,
    })

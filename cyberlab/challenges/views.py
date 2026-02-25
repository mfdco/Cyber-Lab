from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Submission
from .grading import *

# Level 1 flag — hashed once at startup so check_flag can verify it
_LEVEL_1_FLAG = r"flag{Th1s_1s_th3_f1rs7_FlA6}"
_LEVEL_1_HASH = make_password(_LEVEL_1_FLAG)


def challenge_view(request, problem_id):
    if not request.user.is_authenticated:
        return redirect('login')

    result = None

    if request.method == "POST":
        submitted = request.POST.get("flag", "")
        if check_flag(submitted, _LEVEL_1_HASH):
            result = "correct"
        else:
            result = "incorrect"

    return render(request, 'challenges/challenge.html', {
        'user': request.user,
        'result': result,
    })

def submission_check(request):

    flags = {1: "flag{\Th1s_1s_th3_f1rs7_FlA6}", 2: "flag{\S3c0ND_Fl46}"}

    if request.method == "POST":
        user_flag = request.POST['flag']

        if check_flag(user_flag, flags):
            return HttpResponse("Yippy! You've found the correct flag.")
        else :
            return HttpResponse("Wrong flag, keep looking.")

def submission(request, problem_id):
    
    problem = Problem.objects.get(id = problem_id)

    if request.method == "POST":
    
        submitted_flag = request.POST["flag"]

        correct = check_flag(submitted_flag, problem.hashed_flag)

        Submission.objects.create(
            user = request.user,
            problem = problem,
            submitted_flag = submitted_flag,
            is_correct = correct    
        )

        if correct:
            return HttpResponse("Correct")
        else :
            return HttpResponse("Incorrect")
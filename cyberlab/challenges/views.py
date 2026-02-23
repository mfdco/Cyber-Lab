from django.shortcuts import render
from .models import Submission
from .grading import *

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
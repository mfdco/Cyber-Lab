from django.shortcuts import render
from .grading import *

def submission_check(request):

    flags = {1: "flag{\Th1s_1s_th3_f1rs7_FlA6}", 2: "flag{\S3c0ND_Fl46}"}

    if request.method == "POST":
        user_flag = request.POST['flag']

        if check_flag(user_flag, flags):
            return HttpResponse("Yippy! You've found the correct flag.")
        else :
            return HttpResponse("Wrong flag, keep looking.")
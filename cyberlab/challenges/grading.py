# importing django hashing (check_password)
from django.contrib.auth.hashers import check_password

def check_flag(check, hashed_flag):

    return check_password(check, hashed_flag)

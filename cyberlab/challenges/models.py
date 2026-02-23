from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class Problems(models.Model):
    
    problem_title = models.CharField(max_length = 150)
    
    # these flags will be stored in the database
    hashed_flags = models.CharField(max_length = 255, editable = False)

    # these flags will be used as temporary input for the admin page
    flag = models.CharField(max_length = 255)

    def save(self, *args, **kwargs):
        
        if self.flag and not self.flag.startswith("pbkdf2_"):
            self.hashed_flags = make_password(self.flag)
            self.flag = ""
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.problem_title
        

class Submission(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)

    flag_submitted = models.CharField(max_length = 255)

    correct = models.BooleanField(default = False)

    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user} - {self.problem} - {self.correct}"

    

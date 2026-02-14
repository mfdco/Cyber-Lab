from django.db import models

class Problems(models.Model):
    
    problem_title = models.CharField(max_length = 150)
    
    # these flags will be stored in the database
    hashed_flags = models.CharField(max_length = 255)

    # these flags will be used as temporary input for the admin page
    flag = models.CharField(max_length = 255)


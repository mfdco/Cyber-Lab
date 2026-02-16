from django.contrib import admin
from .models import Problems, Submission
from django.contrib.auth.hashers import make_password

admin.site.register(Problems)
admin.site.register(Submission)

class ProblemAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'hashed_flag')
    search_fields = ('title',)
    
    # hide the hashed flag from admin page
    #  exclude = ("hased_flag",)

    # this method will be automatically called by django whenever admin saves a model
    # request = takes HTTP request from browser
    # problem = object of Problem 
    # form = validates input from user
    # change = a boolean where False mean an object is created and True is editing an object
    def save_model(self, request, problem, form, change):
    
        # checks if admin has typed something into the flag field
        if problem.flag:
        
            # takes plaintext flag and hashes it using Django library and stores it in hashed_flag
            problem.hashed_flag = make_password(problem.flag)

            # hide the plaintext version of the flag in admin page
            problem.flag = "" 
        
        # this will call the un-overridden save_model and writes the object into the db 
        super().save_model(request, obj, form, change)

    
# Register your models here.

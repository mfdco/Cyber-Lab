from django.contrib import admin
from .models import Problems, Submission

@admin.register(Problems)
class ProblemAdmin(admin.ModelAdmin):
    
    list_display = ('problem_title', 'section', 'problem_number')

    search_fields = ('problem_title',)

    fields = ('problem_title', 'section', 'problem_number', 'description', 'puzzle_content', 'downloadable_file', 'hints', 'flag')

    # hashed_flags hidden becuase editale = False in the model
    
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'problem', 'correct', 'submitted_at')
    



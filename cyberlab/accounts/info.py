from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }
    def clean_username(self):
        username = self.cleaned_data.get("username")

        # Allow only letters, numbers, and underscores
        if not username.isalnum():
            raise forms.ValidationError("Username can only contain letters and numbers.")

        return username

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        # Custom rule: minimum length
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        # Custom rule: not a common password
        common_passwords = ["password", "12345678", "qwerty", "letmein", "abc123", "admin"]
        if password.lower() in common_passwords:
            raise forms.ValidationError("Password is too common. Choose a stronger one.")

        return password
    

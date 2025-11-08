from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Enter first name")
    last_name = forms.CharField(max_length=50, label="Enter last name")
    email = forms.EmailField(label="Enter email")

class StudentForm(forms.Form):
    class_name = forms.CharField(max_length=100, required=False)
    mentor = forms.CharField(max_length=100, required=False)
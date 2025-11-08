from django.shortcuts import render
from Forms.forms import RegisterForm, StudentForm

# Create your views here.
def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def student_info(request):
    form = StudentForm()
    return render(request, 'student_info.html', {'form': form})
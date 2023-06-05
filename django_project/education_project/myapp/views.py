from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.shortcuts import redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'myapp/student_form.html', {'form': form})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
    return redirect('student_list')
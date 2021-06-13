from django.shortcuts import render
from app.models import Student

def home(request):
    data = {}
    data['students'] = Student.objects.all() 
    return render(request, 'home.html', data)

def view_student(request, pk):
    data = {}
    data['students'] = Student.objects.get(pk=pk)
    return render(request, 'view_student.html', data)
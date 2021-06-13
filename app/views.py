from django.shortcuts import render
from app.models import Student

def home(request):
    data = {}
    data['students'] = Student.objects.all() 
    return render(request, 'home.html', data)
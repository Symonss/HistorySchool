from django.shortcuts import render
from .models import Course
from django.shortcuts import render, get_object_or_404

def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses':courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'detail.html', {'course':course})

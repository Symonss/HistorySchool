from django.shortcuts import render
from .models import Course, Lesson
from django.shortcuts import render, get_object_or_404

def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses':courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course = course.pk)
   
    context = {'course':course, 'lessons':lessons}
    return render(request, 'detail.html', context)

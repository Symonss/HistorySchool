from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.urls import reverse
from mdeditor.fields import MDTextField
from django.utils.html import mark_safe
from markdown import markdown

class Course(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    level = models.CharField(max_length = 100)
    duration = models.IntegerField()
    amount = models.IntegerField(default = 500)
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length = 100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.IntegerField()
    content =  MDTextField(null= True)
    

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))

    def __str__(self):
        return self.title

class Resource(models.Model):
    description = models.CharField(max_length = 100)
    resource = models.FileField(upload_to ='documents/%Y/%m/%d/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'resource'
        verbose_name_plural = 'resources'

    def __str__(self):
        return self.description


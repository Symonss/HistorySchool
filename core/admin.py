from django.contrib import admin
from .models import Course, Lesson, Resource


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Resource)

admin.site.site_header = 'Rawoos Site Administration'
admin.site.site_title = 'Jeremias Teaching and Learning'


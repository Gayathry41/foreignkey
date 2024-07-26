from django.contrib import admin
from foreignkeyapp.models import course,student

# Register your models here.
admin.site.register(course)
admin.site.register(student)
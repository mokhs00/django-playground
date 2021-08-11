from .models import Choice, Person, Question
from django.contrib import admin

# Register your models here.


admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Person)
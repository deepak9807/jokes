from django.contrib import admin

# Register your models here.

from .models import Category,Language,Joke

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Joke)

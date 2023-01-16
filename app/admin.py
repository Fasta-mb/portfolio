from django.contrib import admin

from app.models import Contact, Profile, Project

# Register your models here.

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Project)
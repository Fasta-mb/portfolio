from django.shortcuts import render

from app.models import Profile, Project


# Create your views here.

def home(request):
    profile = Profile.objects.get(id=1)
    projects = profile.project.all()
    context = {'profile': profile, 'projects': projects}
    
    return render(request, 'app/index.html', context)
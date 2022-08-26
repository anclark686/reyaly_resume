from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def experience(request):
    return render(request,
                  "experience/experience.html",
                  {"experience": Experience.objects.all().order_by('-id'),
                   "education": Education.objects.all()})
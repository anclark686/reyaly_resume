from django.shortcuts import render
from .models import Skills, Certification

# Create your views here.
def skills(request):
    return render(request, "skills/skills.html", {"skills": Skills.objects.all(), "certifications": Certification.objects.all()})
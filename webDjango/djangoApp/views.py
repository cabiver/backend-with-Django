from djangoApp.models import Student
from django.shortcuts import render
from .models import Student
def index(request):
    estudiantes = Student.objects.all()
    context = {'clase': 'aprendiendo django', 'estudiantes' : estudiantes}
    return render(request, 'index.html', context)
# Create your views here.

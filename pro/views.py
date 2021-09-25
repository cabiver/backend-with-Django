# from .models import Student
from django.shortcuts import render
# from .models import Student
def index(request):
#     estudiantes = Student.objects.all()
#     context = {'clase': 'aprendiendo django', 'estudiantes' : estudiantes}
#     return render(request, 'index.html', context)
    return render(request, 'example.html')
def big_shot(request):
    return render(request, 'deltarune.html')
def example(request):
    return render(request, 'example.html')
# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'deltarune.html')
def big_shot(request):
    return render(request, 'villanos.html')
def example(request):
    return render(request, 'example.html')

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'deltarune.html')
def big_shot(request):
    return render(request, 'villanos.html')
def charater(request):
    return render(request, 'character.html')


# Create your views here.

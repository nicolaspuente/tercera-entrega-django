from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')
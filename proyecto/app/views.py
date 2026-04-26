from django.shortcuts import render

def inicio(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')
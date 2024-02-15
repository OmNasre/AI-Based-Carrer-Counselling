# views.py
from django.shortcuts import render, redirect
from .models import Question, Option, UserResponse
from .forms import AptitudeTestForm

def aptitude(request):
    return render(request, 'aptitude.html')

def aptitude1(request):
    return render(request, 'aptitude1.html')

def aptitude2(request):
    return render(request, 'aptitude2.html')

def aptitude3(request):
    return render(request, 'aptitude3.html')

def result(request):
    return render(request, 'result.html')

# def aptitude_test_result(request):
#     # Assuming there is no user authentication for simplicity
#     results = UserResponse.objects.all()
#     return render(request, 'result.html', {'results': results})

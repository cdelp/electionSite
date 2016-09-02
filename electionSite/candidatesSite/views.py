from django.shortcuts import render

def index(request):
    return render(request, 'candidatesSite/home.html')

def comparisons(request):
    return render(request, 'candidatesSite/comparisons.html')

def test(request):
    return render(request, 'candidatesSite/test.html')


from django.shortcuts import render


def error_view(request):
    
    return render(request, 'error.html')
    
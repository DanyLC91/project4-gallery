from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Render the index.html template
    return render(request, 'index.html')

def about(request):
    # Render the about.html template
    return render(request, 'about.html')

def exhibition(request):
    # Render the exhibition.html template
    return render(request, 'exhibition.html')
def contact (request):
    return render(request, 'contact.html')
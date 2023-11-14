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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('Hello from Hawtrhorne Fine Art Gallery',
              'We have recieve your message, and one of our agents will contact you son',
              'This is a generated email.Please do not reply',
              'contact@hawthorne.com')    
        return HttpResponse('Form submitted successfully!')
    return render(request, 'contact.html')
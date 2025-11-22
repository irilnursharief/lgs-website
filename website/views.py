from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def service(request):
    return render(request, 'website/service.html')

def contact(request):
    return render(request, 'website/contact.html') 

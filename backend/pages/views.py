from django.shortcuts import render

def home(request):
    context = {
        'title': 'Healthcare AI - Home',
        'welcome_message': 'Welcome to Healthcare AI Solutions'
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'about_text': 'We provide AI-powered healthcare solutions.'
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {
        'title': 'Contact Us',
        'contact_email': 'info@healthcare-ai.com'
    }
    return render(request, 'pages/contact.html', context)
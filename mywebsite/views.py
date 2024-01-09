from django.shortcuts import render

def index(request):
    context = {
        'title': "Home_page",
        'heading': "Halaman_Home_Page",
        'subheading': "Welcom Home",
    }
    
    return render(request, 'index.html', context)
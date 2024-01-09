from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()

    context = {
        'title': "Blog_page",
        'heading': "Halaman_Blog_Page",
        'subheading': "Welcom Blog",
        'categories': categories,
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

def category_post(request, category_post):
    posts = Post.objects.filter(category=category_post)
    categories = Post.objects.values('category').distinct()

    context = {
        'title': "Blog_page",
        'heading': "Halaman_Tampilan_Berdasarkan_Kategory",
        'subheading': "Welcom Blog",
        'categories': categories,
        'posts': posts,
    }
    
    return render(request, 'blog/category.html', context)

def detail(request, slug):
    posts = Post.objects.get(slug=slug)
    categories = Post.objects.values('category').distinct()

    context = {
        'title': "Blog_page",
        'heading': "Halaman_Blog_Page",
        'subheading': "Welcom Blog",
        'categories': categories,
        'posts': posts,
    }
    
    return render(request, 'blog/detail.html', context)

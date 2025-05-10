from django.shortcuts import render
from django.views import View
from . models import Blog

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    

class BlogView(View):
    def get(self, request):
        blog = Blog.objects.all()
        context = {
            'blog':blog
        }
        return render(request, 'blog.html', context)
    

class BlogDetailsView(View):
    def get(self, request, pk):
        return render(request, 'blogDetails.html')
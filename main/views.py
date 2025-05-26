from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . models import Blog, Category
from . forms import CommentModelForm

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
        latest_blog = Blog.objects.all().order_by('-id').first()
        category = Category.objects.all()

        context = {
            'blog':blog,
            'latest':latest_blog,
            'category':category
        }

        return render(request, 'blog.html', context)
    

class BlogDetailsView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, id = pk)
        form = CommentModelForm()

        context = {
            'blog':blog,
            'form':form
        }
        return render(request, 'blogDetails.html', context)
    
    def post(self, request, pk):
        blog = get_object_or_404(Blog, id = pk)
        form = CommentModelForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.blog = blog
            data.save()
            return redirect('blogDetails', pk = pk)
        
        context = {
            'form':form,
            'blog':blog
        }
        return render(request, 'blogDetails.html', context)
    
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
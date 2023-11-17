from django.shortcuts import render
from .models import Post, Comment, Category
from .forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.

def blog_home(request):
    post = Post.objects.all().order_by('-created_on')
    context = {
        'posts' : post,
    }
    return render(request, 'blog/home.html', context)

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    categories = Category.objects.all()    
    context = {
        'posts' : posts,
        'categories' : categories,
    }
    return render(request, 'blog/blog.html', context)

def blog_category(request, category):
    post = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category' : category,
        'posts' : post,
    }
    return render(request, 'blog/category.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        else:
            message = 'Invalid form'
            return render(request, 'blog/details.html', {'form': form, 'message': message})
    comments = Comment.objects.filter(post=post)
    context = {
        'post' : post,
        'comments' : comments,
        'form' : form,
    }
    return render(request, 'blog/details.html', context)

def project_index(request):
    return render(request, 'blog/project.html')

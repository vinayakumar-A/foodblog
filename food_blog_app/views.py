from django.shortcuts import render, get_object_or_404
from .models import Food_Post
from django.utils import timezone
from django.contrib.auth.models import User
from .froms import FoodpostForm
from django.core.paginator import Paginator


# Create your views here.

def food_post_lists(request):
    posts = Food_Post.objects.filter(publish='published').order_by('-created_at')
    paginator = Paginator(posts,3) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'food_blog_app/post_list.html',context)

def post_detail(request, pk):
    post = get_object_or_404(Food_Post, pk=pk)
    context = {'post':post}
    return render(request, 'food_blog_app/post_detail.html',context )

def add_post(request):
    if request.method == 'POST':
        form = FoodpostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
    else:
        form = FoodpostForm()
    context = {'form':form}
    return render(request, 'food_blog_app/add_post.html',context)


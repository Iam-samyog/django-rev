from django.shortcuts import render

from django.views.generic import ListView,TemplateView,DetailView
from .models import Post

class HomePageView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='all_posts_list'

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'
    context_object_name='post'

class AboutViewPage(TemplateView):
    template_name="about.html"
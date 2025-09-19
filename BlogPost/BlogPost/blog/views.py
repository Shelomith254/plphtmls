from django.shortcuts import render
from .models import Post,Comment

# Create your views here.
def homepage(request):
    Post=Post.objects.all()
    return render(request,'blog/homepage.html')
def post_detail(request,Comment):
    Post=Post.objects.get(Comment=Comment)
    return render(request,'blog/post_detail.html',{'post':Post})


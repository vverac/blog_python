from django.shortcuts import render
from .models import Post, Comment
# Create your views here.

def post_list(request):
  # traemos los objetos ordenados por el dia en que se crearon
  posts = Post.objects.all().order_by('-created_at')
  # traeremos todo esto , los post
  return render ( request,'blog/post_list.html', {'posts':posts})

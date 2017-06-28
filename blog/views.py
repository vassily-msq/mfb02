from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone as tz

# Create your views here.
def post_list(request):
    published = Post.objects.filter(date_published__lte = tz.now()).order_by('date_published')
    r=render(request, 'blog/post_list.html', {'posts': published})
    return r

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

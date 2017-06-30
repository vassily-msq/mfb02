from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.utils import timezone as tz
from blog.forms import PostForm

# Create your views here.
def post_list(request):
    published = Post.objects.filter(date_published__lte = tz.now()).order_by('date_published')
    r=render(request, 'blog/post_list.html', {'posts': published})
    return r

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        # print('POST')
        # print('--------REQUEST----------')
        # print(request)
        # print('-------------------------')
        form = PostForm(request.POST)
        # a = "-"*15
        # print(a)
        # print(form)
        # print(a)
        # print("Construct PostForm w / data from the form")
        if form.is_valid():
            # print(1)
            post = form.save(commit=False)
            # print(2)
            post.author = request.user
            # print(3)
            post.date_published = tz.now()
            # print(4)
            post.save()
            # print(5)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.date_published = tz.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

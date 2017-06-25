from django.shortcuts import render

# Create your views here.
def post_list(request):
    r=render(request, 'blog/post_list.html', {})
    return r

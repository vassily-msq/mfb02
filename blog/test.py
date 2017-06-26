from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone as tz

a = '-----'
print(a)
print('Entire set:')
allrecords = Post.objects.all()
for rec in allrecords:
    print(rec.title)
print(a)
print('Published posts:')
published = Post.objects.filter(date_published__lte = tz.now())
for rec in published:
    print(rec.title)
print(a)

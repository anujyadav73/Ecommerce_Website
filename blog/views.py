from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_index(request):
    return render(request, 'blog/index.html')
#    return HttpResponse("Hello, world. You're at the blog index.")
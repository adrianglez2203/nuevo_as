
from django.shortcuts import render

from blogs import models
from .forms import CommentForm
# Create your views here.

def post_comments(request):

    return render(request, 'blogs/blog_index_page.html')





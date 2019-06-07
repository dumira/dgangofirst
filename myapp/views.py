from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse('<h1>Blog home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

posts=[
    {
        'author': 'aa',
        'title': 'bp1',
        'content': 'First post',
        'date':'27 may'
    },

        {
        'author': 'abba',
        'title': 'bp2',
        'content': 'secound post',
        'date':'29 may'
    }
]

def home(request):

    context={
        'posts': posts
    }
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html', {'title':'About'})